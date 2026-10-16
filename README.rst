Diátaxis
========================

中文版本与 GitHub Pages 部署
---------------------------

本 fork 使用 ``translation/zh_CN/LC_MESSAGES`` 中的简体中文翻译，
中文站点地址为 https://sanchuanhehe.github.io/diataxis-documentation-framework/ 。

在 GitHub 仓库的 Settings → Pages 中将 Source 设置为 GitHub Actions。
推送到 ``main`` 后自动构建并部署；也可以在 Actions 中手动运行
``Deploy Chinese documentation to GitHub Pages``。Pull request 只构建、不部署。

本地预览::

    python3 -m venv env
    source env/bin/activate
    pip install -r requirements.txt
    GITHUB_PAGES=true sphinx-build -b dirhtml -D language=zh_CN source _build/html
    python -m http.server 8000 --directory _build/html

访问 http://localhost:8000/ 。未翻译的段落会回退到英文；更新对应的
``.po`` 文件并推送到 ``main`` 即可重新发布。英文、波兰文切换链接指向上游站点。
原作者和 CC-BY-SA 4.0 许可信息保留如下。

中文术语与图示
~~~~~~~~~~~~~~

中文版本以“知与行、学与用”概括两个维度：知指认知与理解，行指行动与实践；
学指习得知识与技能，用指运用知识与技能。它们区分文档支持的活动与用户当前的目的，
不表示用户水平或固定的先后阶段。理论正文保留原概念的完整定义。

这套写法已固化在 ``source/images/zh_CN/*.svg`` 全部中文图示中，正文用词必须与图示一致：
英文以粗体标出的框架术语（``**action**``、``**cognition**`` 等）一律译为
``**行（行动）**``、``**知（认知）**``、``**学（习得）**``、``**用（应用）**``；
坐标轴标题 ``Action/cognition`` 与 ``Acquisition/application`` 固定译作“知与行”“学与用”。

中文框架示意图位于 ``source/images/zh_CN/``，采用可编辑文字的 SVG 格式，
由上游图示翻译、重绘，沿用本项目的 CC-BY-SA 4.0 许可。
Sphinx 在 ``language=zh_CN`` 时自动选用同名中文 SVG；没有对应 SVG 的图片
使用原图。修改 SVG 后重新构建即可预览。
核心框架图的可复用绘制逻辑保存在 ``scripts/generate-core-diagrams.py``；
修改该脚本后运行 ``python3 scripts/generate-core-diagrams.py`` 可重新生成九张核心图。

翻译规范与工具链
~~~~~~~~~~~~~~~~

翻译与校订的依据是 ``translation/zh_CN/STYLE.md``，其中规定了术语表、
“知/行/学/用”框架的用法、强调标记与 Sphinx 角色的处理、中文标点排版规则，
以及常见译文腔的改法。改动 ``.po`` 前请先通读该文件。

``tools/`` 下提供四个脚本（均依赖 ``requirements.txt``，用虚拟环境解释器运行）：

``tools/dump-pairs.py``
    以中英对照形式打印某个 ``.po``，便于通读：``python tools/dump-pairs.py tutorials``。

``tools/apply-translations.py``
    把 ``msgid -> 新 msgstr`` 的 JSON 安全套用到 ``.po``；只替换 ``msgstr`` 块，
    文件头、注释、``msgid``、顺序与 flags 逐字节保留，并按显示宽度重新折行。
    **不要手工编辑 ``.po`` 语法**，一律走这条路径。

``tools/check-po.py``
    结构校验：Sphinx 角色目标、`` ``字面量`` ``、URL、强调标记的种类与数量是否与英文
    逐一对应，以及中文标点排版（标记两侧空格、全角标点、省略号）与术语禁译。

``tools/check-render.py``
    渲染级校验：用与站点构建相同的 docutils 设置逐条解析译文，确认行内标记真的会被
    解析成粗体／斜体／字面量，而不是把星号原样显示出来。**这一项无法靠肉眼或句法检查替代。**

``tools/check-terms.py``
    跨文件术语一致性校验，并强制“知/行/学/用”框架术语的注解形式。

``tools/diff-report.py``
    以 git ``HEAD`` 为基准，生成“原文 → 原译 → 新译”的改动报告，便于人工审校。

``tools/verify.sh``
    交付前的一站式验证：结构校验 → 渲染级校验 → 术语校验 → 构建（``-W`` 视警告为错误）
    → 产物抽查。

中文排版的一个前提
~~~~~~~~~~~~~~~~~~

docutils 默认要求行内标记的开头紧跟在空白或标点之后，结尾之后也必须是空白或标点。
汉字属于 Unicode 字母类，两条都不满足，因此默认情况下 ``中文**粗体**中文`` 不会被解析，
而是原样显示两个星号。中文没有词间空格，若为迁就这条规则在正文里插入空格，版面会显得松散。

``source/docutils.conf`` 为此开启了 docutils 的 ``character-level-inline-markup``，
取消位置限制，使标记紧贴汉字也能正确解析。该设置对英文构建**没有任何影响**
（开启前后的英文 HTML 逐字节相同）。若改动该文件或调整构建方式，
务必重跑 ``tools/check-render.py``。

完整验证::

    bash tools/verify.sh

上游项目
--------

Diátaxis is a way of thinking about and doing documentation.

It prescribes approaches to content, architecture and form that emerge from a systematic approach to understanding the needs of documentation users.

Published at https://diataxis.fr

Author: `Daniele Procida <https://vurt.org>`_

I enjoy hearing about other people’s experiences with Diátaxis and read everything I receive.

I appreciate all the interest and do my best to reply, but I get a considerable quantity of email related to Diátaxis and I can’t promise to respond to every message.

If you’d like to discuss Diátaxis with other users, please see the `#diataxis <https://www.writethedocs.org/slack/> channel on the Write the Docs Slack group`_, or the `Discussions <https://github.com/evildmp/diataxis-documentation-framework/discussions>`_ section of `the GitHub repository for this website <https://github.com/evildmp/diataxis-documentation-framework>`_.

Licence: `CC-BY-SA 4.0 <https://creativecommons.org/licenses/by-sa/4.0/>`_
