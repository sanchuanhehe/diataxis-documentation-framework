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

中文框架示意图位于 ``source/images/zh_CN/``，采用可编辑文字的 SVG 格式，
由上游图示翻译、重绘，沿用本项目的 CC-BY-SA 4.0 许可。
Sphinx 在 ``language=zh_CN`` 时自动选用同名中文 SVG；没有对应 SVG 的图片
使用原图。修改 SVG 后重新构建即可预览。
核心框架图的可复用绘制逻辑保存在 ``scripts/generate-core-diagrams.py``；
修改该脚本后运行 ``python3 scripts/generate-core-diagrams.py`` 可重新生成九张核心图。

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
