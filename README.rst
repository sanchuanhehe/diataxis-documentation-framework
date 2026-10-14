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
