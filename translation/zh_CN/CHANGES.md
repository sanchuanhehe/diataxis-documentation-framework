# Diátaxis 简体中文译文修订报告

本报告由 `tools/diff-report.py` 生成，以 git `HEAD` 的译文为「旧」，工作区当前译文为「新」。
格式：`EN` 英文原文 / `旧` 修订前中文 / `新` 修订后中文。

修订依据：[`translation/zh_CN/STYLE.md`](STYLE.md)。
校验方式：`bash tools/verify.sh`（结构 → 渲染 → 术语 → 构建 → 产物）。

```
application               15 条  改动  13
colophon                  20 条  改动  16
compass                   33 条  改动  20
explanation               57 条  改动  35
foundations               38 条  改动  18
how-to-guides             70 条  改动  64
how-to-use-diataxis       34 条  改动  32
index                     32 条  改动  16
map                       73 条  改动  34
news                       9 条  改动   3
quality                   68 条  改动  58
reference                 45 条  改动  36
reference-explanation     22 条  改动  19
sphinx                     6 条  改动   2
start-here                78 条  改动  47
theory                    15 条  改动   8
translation               34 条  改动  23
tutorials                107 条  改动  92
tutorials-how-to          71 条  改动  65

合计：827 条，改动 601 条
```
application               15 条  改动  13

  ── [application]
  EN | The pages in this section are concerned with putting Diátaxis into practice.
  旧 | 本节页面讨论如何将 Diátaxis 付诸实践。
  新 | 本节各页，讲的都是如何把 Diátaxis 付诸实践。

  ── [application]
  EN | Diátaxis is underpinned by :doc:`systematic theoretical principles <theory>`, but understanding them is not necessary to make effective use of the system.
  旧 | Diátaxis 以 :doc:`系统化的理论原则 <theory>` 为基础，但不必理解它们，也能有效使用这一体系。
  新 | Diátaxis 以:doc:`系统化的理论原则 <theory>`为支撑，但要有效运用这套体系，并不需要先理解它们。

  ── [application]
  EN | Diátaxis is primarily intended as a pragmatic approach for people working on documentation. Most of the key principles required to put it into practice successfully can be grasped intuitively.
  旧 | Diátaxis 主要是一种面向文档工作者的务实方法。要成功实践它，所需的大多数关键原则都可以凭直觉理解。
  新 | Diátaxis 首先是一种务实的方法，面向做文档的人。要把它成功付诸实践，所需的关键原则大多凭直觉就能掌握。

  ── [application]
  EN | Don't wait to understand Diátaxis before you start trying to put it into practice. Not only do you not need to understand it all to make use of it, you will not understand it until you have started using it (this itself is a Diátaxis principle).
  旧 | 不要等到理解 Diátaxis 后才尝试实践它。你不仅无需完全理解它就能使用，而且在开始使用之前也不会真正理解它（这本身就是一项 Diátaxis 原则）。
  新 | 别等理解了 Diátaxis 才动手实践。要用它，你不必先全都理解；如果不开始用，你也理解不了它（这本身就是一项 Diátaxis 原则）。

  ── [application]
  EN | As soon as you feel you have picked up an idea that seems worth applying to your work, try applying it. Come back here when you need more clarity or reassurance. Iterate between your work and reflecting on your work.
  旧 | 一旦觉得掌握了某个值得用于工作的想法，就去试一试。需要更多清晰认识或信心时，再回到这里。让实际工作与对工作的反思反复迭代。
  新 | 一旦觉得抓到了什么想法，值得用在自己工作上，就动手试试。需要更清楚一些，或者需要一点安心时，再回到这里。在工作与对工作的反思之间来回迭代。

  ── [application]
  EN | At the core of Diátaxis are the four different kinds of documentation it identifies. If you're encountering Diátaxis for the first time, start with these pages.
  旧 | Diátaxis 的核心是它识别出的四种不同文档类型。若你是第一次接触 Diátaxis，请从这些页面开始。
  新 | Diátaxis 的核心，是它识别出的四种不同文档类型。如果你是第一次接触 Diátaxis，就从这几页开始。

  ── [application]
  EN | :doc:`tutorials` - learning-oriented experiences
  旧 | :doc:`tutorials` ——面向学习的体验
  新 | :doc:`tutorials`——面向学习的体验

  ── [application]
  EN | :doc:`how-to-guides` - goal-oriented directions
  旧 | :doc:`how-to-guides` ——面向目标的操作指引
  新 | :doc:`how-to-guides`——面向目标的方向指引

  ── [application]
  EN | :doc:`reference` - information-oriented technical description
  旧 | :doc:`reference` ——面向信息的技术描述
  新 | :doc:`reference`——面向信息的技术描述

  ── [application]
  EN | :doc:`explanation` - understanding-oriented discussion
  旧 | :doc:`explanation` ——面向理解的论述
  新 | :doc:`explanation`——面向理解的论述

  ── [application]
  EN | Diátaxis prescribes principles that guide action. These translate into particular ways of working, with implications for documentation process and execution. Once you've made your first start, the tools and methods outlined here will help smooth your way.
  旧 | Diátaxis 提供引导行动的原则。它们转化为特定的工作方式，并影响文档的流程与执行。完成第一步后，这里概述的工具和方法将帮助你更顺利地前进。
  新 | Diátaxis 规定了一些引导行动的原则。这些原则会转化为特定的工作方式，对文档的流程与执行都有影响。一旦起步，这里列出的工具和方法会帮你把路走顺。

  ── [application]
  EN | :doc:`compass` - a simple tool for direction-finding
  旧 | :doc:`compass` ——用于辨明方向的简单工具
  新 | :doc:`compass`——一件辨明方向的简单工具

  ── [application]
  EN | :doc:`Workflow <how-to-use-diataxis>` in Diátaxis
  旧 | Diátaxis 中的 :doc:`工作流程 <how-to-use-diataxis>`
  新 | Diátaxis 中的:doc:`工作流程 <how-to-use-diataxis>`
colophon                  20 条  改动  16

  ── [colophon]
  EN | Colophon
  旧 | 版权与说明
  新 | 版本说明

  ── [colophon]
  EN | Diátaxis is the work of `Daniele Procida <https://vurt.eu>`_.
  旧 | Diátaxis 是 `Daniele Procida <https://vurt.eu>`_ 的作品。
  新 | Diátaxis 是 `Daniele Procida <https://vurt.eu>`_ 的成果。

  ── [colophon]
  EN | It has been developed over a number of years, and continues to be elaborated and explored.
  旧 | 它历经多年发展，仍在不断完善与探索。
  新 | 它历经多年发展，至今仍在不断打磨、探索。

  ── [colophon]
  EN | `Email me <daniele@vurt.org>`_. I enjoy hearing about other people's experiences with Diátaxis and read everything I receive.
  旧 | `给我发邮件 <daniele@vurt.org>`_。我乐于听到他人使用 Diátaxis 的经验，也会阅读收到的每一封来信。
  新 | `给我发邮件 <daniele@vurt.org>`_。我乐于听人谈他们使用 Diátaxis 的经验，收到的每一封来信也都会读。

  ── [colophon]
  EN | I appreciate all the interest and do my best to reply, but I get a considerable quantity of email related to Diátaxis and I can't promise to respond to every message.
  旧 | 我感谢大家的关注，并会尽力回复；但与 Diátaxis 有关的邮件数量很多，无法保证逐一答复。
  新 | 感谢大家的关注，我也会尽力回复；只是 Diátaxis 相关的邮件相当多，我无法保证每封都回。

  ── [colophon]
  EN | If you'd like to discuss Diátaxis with other users, please see the *#diataxis* channel on the `Write the Docs Slack group <https://www.writethedocs.org/slack/>`_, or the `Discussions <https://github.com/evildmp/diataxis-documentation-framework/discussions>`_ section of the `GitHub repository for this website <https://github.com/evildmp/diataxis-documentation-framework>`_.
  旧 | 如果希望与其他用户讨论 Diátaxis，请参阅 `Write the Docs Slack 群组 <https://www.writethedocs.org/slack/>`_ 中的 *#diataxis* 频道，或访问本网站 `GitHub 仓库 <https://github.com/evildmp/diataxis-documentation-framework>`_ 的 `Discussions <https://github.com/evildmp/diataxis-documentation-framework/discussions>`_ 区域。
  新 | 如果你想和其他用户讨论 Diátaxis，请看 `Write the Docs Slack 群组 <https://www.writethedocs.org/slack/>`_ 里的 *#diataxis* 频道，或者到本网站的 `GitHub 仓库 <https://github.com/evildmp/diataxis-documentation-framework>`_ 的 `Discussions <https://github.com/evildmp/diataxis-documentation-framework/discussions>`_ 板块。

  ── [colophon]
  EN | You can find `an earlier presentation of some of these ideas <https://documentation.divio.com>`_, that I created while working at Divio between 2014-2021. I still agree with most of it, though there are several aspects that I now think I got wrong.
  旧 | 你可以找到我在 2014 至 2021 年于 Divio 工作时制作的 `这些想法的早期介绍 <https://documentation.divio.com>`_。其中大部分观点我至今仍认同，不过也有若干方面如今看来当时理解有误。
  新 | 2014 至 2021 年我在 Divio 工作期间，写过一份`这些想法的早期介绍 <https://documentation.divio.com>`_。其中大部分内容我至今仍然认同，不过有几点我认为自己当时搞错了。

  ── [colophon]
  EN | The original context for the Diátaxis approach was limited to software product documentation.
  旧 | Diátaxis 方法最初的语境仅限于软件产品文档。
  新 | Diátaxis 这套方法起初的语境仅限于软件产品文档。

  ── [colophon]
  EN | In 2021 I was awarded a Fellowship of the `Software Sustainability Institute <http://software.ac.uk/blog/sorry-state-usable-software-open-science-results-open-science-retreat>`_, to explore its application in scientific research contexts. More recently I've explored its application in internal corporate documentation, organisational management and education, and also its application at scale. This work is on-going.
  旧 | 2021 年，我获得 `软件可持续性研究所 <http://software.ac.uk/blog/sorry-state-usable-software-open-science-results-open-science-retreat>`_ 的研究员资助，以探索其在科研语境中的应用。近来我又探索了它在企业内部文档、组织管理、教育及大规模场景中的应用。这项工作仍在继续。
  新 | 2021 年，`软件可持续性研究所 <http://software.ac.uk/blog/sorry-state-usable-software-open-science-results-open-science-retreat>`_ 授予我一项研究员资助，用以探索它在科学研究中的应用。后来我又探索了它在企业内部文档、组织管理、教育中的应用，以及规模化应用。这项工作仍在继续。

  ── [colophon]
  EN | Other people have corresponded with me to share their experience of applying Diátaxis to note-taking systems and even as part of a systematic approach to household management.
  旧 | 还有其他人与我通信，分享将 Diátaxis 应用于笔记系统，甚至作为家庭管理系统化方法一部分的经验。
  新 | 也有人写信给我，分享他们把 Diátaxis 用到笔记系统上的经验，甚至把它当作家庭管理系统化方法的一部分。

  ── [colophon]
  EN | To cite Diátaxis, please refer to :doc:`this website, diataxis.fr <index>`.
  旧 | 如需引用 Diátaxis，请参阅 :doc:`本网站 diataxis.fr <index>`。
  新 | 引用 Diátaxis，请参见:doc:`本网站 diataxis.fr <index>`。

  ── [colophon]
  EN | The Git repository for the source material contains a citation file, `CITATION.cff <https://github.com/evildmp/diataxis-documentation-framework/blob/main/CITATION.cff>`_.
  旧 | 源材料的 Git 仓库包含一份引用文件：`CITATION.cff <https://github.com/evildmp/diataxis-documentation-framework/blob/main/CITATION.cff>`_。
  新 | 原始资料的 Git 仓库中有一份引用文件 `CITATION.cff <https://github.com/evildmp/diataxis-documentation-framework/blob/main/CITATION.cff>`_。

  ── [colophon]
  EN | APA and BibTeX metadata are available from the *Cite this repository* option at https://github.com/evildmp/diataxis-documentation-framework.
  旧 | 可通过 https://github.com/evildmp/diataxis-documentation-framework 的 *Cite this repository* 选项获取 APA 和 BibTeX 元数据。
  新 | 在 https://github.com/evildmp/diataxis-documentation-framework 上，可以通过 *Cite this repository* 功能获取 APA 与 BibTeX 元数据。

  ── [colophon]
  EN | You can also submit a pull request to suggest an improvement or correction, or `file an issue <https://github.com/evildmp/diataxis-documentation-framework/issues>`_.
  旧 | 你也可以提交拉取请求以建议改进或修正，或 `提交 issue <https://github.com/evildmp/diataxis-documentation-framework/issues>`_。
  新 | 你也可以提交拉取请求，提个改进或修正，或者`提交 issue <https://github.com/evildmp/diataxis-documentation-framework/issues>`_。

  ── [colophon]
  EN | Diátaxis is now used in several hundred projects and it is no longer possible for me to keep up with requests to have projects listed here as examples of Diátaxis adoption.
  旧 | Diátaxis 现已用于数百个项目，因此我已无法继续处理将项目列为 Diátaxis 采用示例的请求。
  新 | 如今采用 Diátaxis 的项目已有数百个；对于“把我这个项目列在这里，作为 Diátaxis 应用示例”的请求，我已无力一一应付。

  ── [colophon]
  EN | This website is built with `Sphinx <https://www.sphinx-doc.org>`_ and hosted on `Read the Docs <http://readthedocs.org>`_, using a modified version of `Pradyun Gedam <https://pradyunsg.me/>`_'s `Furo <https://github.com/pradyunsg/furo>`_ theme.
  旧 | 本网站使用 `Sphinx <https://www.sphinx-doc.org>`_ 构建，托管在 `Read the Docs <http://readthedocs.org>`_，使用的是 `Pradyun Gedam <https://pradyunsg.me/>`_ 的 `Furo <https://github.com/pradyunsg/furo>`_ 主题的修改版。
  新 | 本网站用 `Sphinx <https://www.sphinx-doc.org>`_ 构建，托管在 `Read the Docs <http://readthedocs.org>`_ 上，用的是 `Pradyun Gedam <https://pradyunsg.me/>`_ 的 `Furo <https://github.com/pradyunsg/furo>`_ 修改版主题。
compass                   33 条  改动  20

  ── [compass]
  EN | The Diátaxis map is an effective reminder of the different kinds of documentation and their relationship, and it accords well with intuitions about documentation.
  旧 | Diátaxis 地图能有效提醒我们不同文档类型及其关系，也很符合人们对文档的直觉。
  新 | Diátaxis 地图能有效提醒我们文档有哪些不同类型、彼此是什么关系，也很贴合人们对文档的直觉。

  ── [compass]
  EN | However intuition is not always to be relied upon. Often when working with documentation, an author is faced with the question: *what form of documentation is this?* or *what form of documentation is needed here?* - and no obvious, intuitive answer.
  旧 | 但直觉并非总是可靠。处理文档时，作者常会面对这样的问题： *这是什么形式的文档？* 或 *这里需要什么形式的文档？* ——而没有明显、直观的答案。
  新 | 然而直觉并不总是靠得住。跟文档打交道时，作者常常碰上这样一个问题：*这是什么形式的文档？*或者*这里需要什么形式的文档？*——答案却既不明显，也不直观。

  ── [compass]
  EN | Worse, sometimes intuition provides an immediate answer that is also wrong.
  旧 | 更糟的是，有时直觉会立即给出答案，但答案同样是错误的。
  新 | 更糟的是，有时候直觉立刻给出一个答案——而那个答案同样是错的。

  ── [compass]
  EN | A map is most powerful in unfamiliar territory when we also have a compass to guide us.
  旧 | 在陌生领域，地图与能指引我们的指南针相配合时，最能发挥作用。
  新 | 身处陌生之地，若再有一只指南针为我们指引方向，地图才最见威力。

  ── [compass]
  EN | The Diátaxis compass is something like a truth-table or decision-tree of documentation. It reduces a more complex, two-dimensional problem to its simpler parts, and provides the author with a course-correction tool.
  旧 | Diátaxis 指南针类似于文档的真值表或决策树。它把较复杂的二维问题化为更简单的部分，并为作者提供修正方向的工具。
  新 | Diátaxis 指南针有点像文档的真值表或决策树。它把更复杂的二维问题拆解成几个更简单的部分，也为作者提供了一件校正方向的工具。

  ── [compass]
  EN | acquisition of skill
  旧 | 技能习得（学）
  新 | 技能的习得（学）

  ── [compass]
  EN | application of skill
  旧 | 技能应用（用）
  新 | 技能的应用（用）

  ── [compass]
  EN | The compass can be applied equally to user situations that need documentation, or to documentation itself that perhaps needs to be moved or improved. Like many good tools, it's surprisingly banal.
  旧 | 指南针同样可用于需要文档支持的用户情境，也可用于可能需要移动或改进的文档本身。和许多好工具一样，它出人意料地平淡无奇。
  新 | 指南针既能用在需要文档的用户处境上，也能用在文档本身——它或许需要挪个位置，或需要改进。和许多好工具一样，它出人意料地平淡无奇。

  ── [compass]
  EN | To use the compass, just two questions need to be asked: *action or cognition?* *acquisition or application?*
  旧 | 使用指南针，只需问两个问题： *知还是行？* *学还是用？*
  新 | 要用指南针，只需问两个问题：*行（行动）还是知（认知）？* *学（习得）还是用（应用）？*

  ── [compass]
  EN | And it yields the answer.
  旧 | 答案便会得出。
  新 | 答案便会浮现。

  ── [compass]
  EN | The compass is particularly effective when you think that you (or even the documentation in front of you) are doing one thing - but you are troubled by a sense of doubt, or by some difficulty in the work. The compass forces you to stop and reconsider.
  旧 | 当你认为自己（或眼前的文档）正在做某件事，但又因怀疑或工作中的某种困难而不安时，指南针尤其有效。它迫使你停下来重新审视。
  新 | 当你以为自己（甚至你眼前的那份文档）正在做某件事——心里却有一丝疑虑，或者在工作中遇到某种困难时，指南针尤其管用。它逼你停下来，重新掂量。

  ── [compass]
  EN | Especially when you are trying to find your initial bearings, use the compass's terms flexibly; don't get fixated on the exact names.
  旧 | 尤其是在最初辨明方向时，应灵活使用指南针的术语；不要执着于名称的精确表述。
  新 | 尤其是在初辨方向时，要灵活使用指南针的术语；不要死抠确切的名称。

  ── [compass]
  EN | *action*: practical steps, doing
  旧 | *行（行动）*：实际步骤、动手做
  新 | *行（行动）*：实际步骤，动手做

  ── [compass]
  EN | *cognition*: theoretical or propositional knowledge, thinking
  旧 | *知（认知）*：理论性或命题性知识、思考
  新 | *知（认知）*：理论性知识或命题性知识，思考

  ── [compass]
  EN | *acquisition*: study
  旧 | *学（习得）*：学习知识与技能
  新 | *学（习得）*：学习

  ── [compass]
  EN | *application*: work
  旧 | *用（应用）*：运用知识与技能开展工作
  新 | *用（应用）*：工作

  ── [compass]
  EN | And the questions themselves can also be used in different ways:
  旧 | 这些问题本身也可以用不同方式提出：
  新 | 这些问题本身，也可以有几种不同的问法：

  ── [compass]
  EN | Do I think I am writing for *x* or *y*?
  旧 | 我认为自己是在为 *x* 还是 *y* 写作？
  新 | 我以为自己是为 *x* 还是 *y* 而写？

  ── [compass]
  EN | Is this writing in front of me engaged in *x* or *y*?
  旧 | 眼前这段文字是在进行 *x* 还是 *y*？
  新 | 我眼前这段文字是在做 *x* 还是 *y*？

  ── [compass]
  EN | And try applying them close-up, at the level of sentences and words, or from a wider perspective, considering an entire document.
  旧 | 还可以近距离地在句子和词语层面应用它们，或从更广阔的角度审视整篇文档。
  新 | 用法上也不妨拉近拉远：近到句子和词语的层面去套用它们，或拉远到整篇文档，从更大的角度去看。
explanation               57 条  改动  35

  ── [explanation]
  EN | Explanation is a discursive treatment of a subject, that permits *reflection*. Explanation is **understanding-oriented**.
  旧 | 解释说明是对主题进行论述式的处理，让人能够 *反思*；它是 **面向理解** 的。
  新 | 解释说明是对一个主题的论述，它容许*反思*。解释说明**面向理解**。

  ── [explanation]
  EN | Explanation deepens and broadens the reader's understanding of a subject. It brings clarity, light and context.
  旧 | 解释说明加深并拓宽读者对主题的理解，带来清晰、启发和语境。
  新 | 解释说明加深并拓宽读者对主题的理解，带来清晰、光亮与背景。

  ── [explanation]
  EN | Explanation - understanding oriented, theoretical knowledge, that serves our study
  旧 | 解释说明——面向理解，以理论性知识（知）服务于技能习得（学）
  新 | 解释说明——面向理解，以理论性知识（知）服务于技能的习得（学）

  ── [explanation]
  EN | The concept of *reflection* is important. Reflection occurs *after* something else, and depends on something else, yet at the same time brings something new - shines a new light - on the subject matter.
  旧 | *反思* 这一概念很重要。反思发生在其他事物 *之后*，依赖于其他事物，却同时为主题带来新东西——以新的光线照亮它。
  新 | *反思*这一概念很重要。反思发生在别的事物*之后*，依赖于别的事物，却同时又为主题带来新的东西——投下一道新的光。

  ── [explanation]
  EN | The perspective of explanation is higher and wider than that of the other three types. It does not take the user's eye-level view, as in a how-to guide, or a close-up view of the machinery, like reference material. Its scope in each case is a topic - "an area of knowledge", that somehow has to be bounded in a reasonable, meaningful way.
  旧 | 解释说明的视角比其他三种类型更高、更宽。它不像实践指南那样采取用户平视的视角，也不像参考资料那样近距离观察设备。在每一种情形下，它所处理的范围都是一个主题——“一个知识领域”，必须以合理且有意义的方式界定。
  新 | 解释说明的视角，比其他三类都更高、更宽。它不像实践指南那样，取用户平视的视角；也不像参考资料那样，给系统来一个特写。在每一种情形下，它的范围都是一个主题——“一个知识领域”，而这个主题总得设法划出合理而有意义的边界。

  ── [explanation]
  EN | For the user, explanation joins things together. It's an answer to the question: *Can you tell me about ...?*
  旧 | 对用户而言，解释说明把事物联结起来。它回答的问题是： *你能讲讲……吗？*
  新 | 对用户而言，解释说明把事物联结起来。它回答的是这样一个问题：*你能跟我讲讲……吗？*

  ── [explanation]
  EN | It's documentation that it makes sense to read while away from the product itself (one could say, explanation is the only kind of documentation that it might make sense to read in the bath).
  旧 | 它是离开产品本身后阅读仍有意义的文档（可以说，解释说明是唯一可能适合在泡澡时阅读的文档）。
  新 | 它是一种离开产品本身去读也说得通的文档（可以说，解释说明是唯一一种在泡澡时读也说得通的文档）。

  ── [explanation]
  EN | Explanation  is characterised by its distance from the active concerns of the practitioner. It doesn't have direct implications for what they do, or for their work. This means that it's sometimes seen as being of lesser importance. That's a mistake; it may be less *urgent* than the other three, but it's no less *important*. It's not a luxury. No practitioner of a craft can afford to be without an understanding of that craft, and needs the explanatory material that will help weave it together.
  旧 | 解释说明的特点是与实践者的当下关切保持距离。它不直接影响实践者的行动或工作，因此有时被认为不那么重要。这是错误的：它可能不如其他三类 *紧迫*，但重要性却毫不逊色。它不是奢侈品。任何技艺的实践者都不能缺少对该技艺的理解，需要能帮助把知识编织在一起的解释性材料。
  新 | 解释说明的特点，在于它与实践者当下所操心的实务保持着距离。它对他们做什么、对他们的工作，都没有直接影响，因此有时会被看作次要。这是错的：论*紧迫*，它或许比不上其他三类；论*重要*，它毫不逊色。它不是奢侈品。任何一门技艺的实践者，都不能缺少对本门技艺的理解，也都需要解释性材料，帮他把这份理解编织成网。

  ── [explanation]
  EN | Your explanation documentation doesn't need to be called *Explanation*. Alternatives include:
  旧 | 你的解释性文档不必命名为 *解释说明*。可选名称包括：
  新 | 你的解释说明文档，不必叫*解释说明*。还可以叫这些名字：

  ── [explanation]
  EN | The word *explanation* - and its cognates in other languages - refer to *unfolding*, the revelation of what is hidden in the folds. So explanation brings to the light things that were implicit or obscured.
  旧 | *explanation* 一词及其在其他语言中的同源词，指向“展开”，即揭示藏在褶皱中的事物。因此，解释说明使原本隐含或遮蔽的事物显露出来。
  新 | *explanation* 一词——以及其他语言中的同源词——指向*展开*，即把藏在褶皱里的东西揭示出来。所以，解释说明把原本隐含或被遮蔽的事物带到光亮处。

  ── [explanation]
  EN | Similarly, words that mean *understanding* share roots in words meaning to hold or grasp (as in *comprehend*). That's an important part of understanding, to be able to hold something or be in possession of it. Understanding seals together the other components of our mastery of a craft, and makes it safely our own.
  旧 | 同样，意为 *理解* 的词常与意为持有或抓住的词共享词根（如 *comprehend*）。这是理解的重要部分：能够持有某物，或将其据为己有。理解把掌握技艺的其他组成部分黏合起来，使其稳妥地成为我们自己的能力。
  新 | 同样，表示*理解*的词，与表示持有、抓取的词同源（如 *comprehend*）。能够抓住一样东西，把它攥在手里，这正是理解的重要一环。理解把我们掌握一门技艺的其他各个部件封合成一体，让它安稳地归我们所有。

  ── [explanation]
  EN | Understanding doesn't *come from* explanation, but explanation is required to form that web that helps hold everything together. Without it, the practitioner's knowledge of their craft is loose and fragmented and fragile, and their exercise of it is *anxious*.
  旧 | 理解并不 *来自* 解释说明，但解释说明是织就那张联系一切之网所必需的。没有它，实践者关于技艺的知识会松散、零碎而脆弱，实践时便会感到 *焦虑*。
  新 | 理解并不*来自*解释说明，但要织成那张把一切拢在一起的网，解释说明不可或缺。没有它，实践者对自身技艺的知识就松散、零碎而脆弱，实践起来也*焦虑不安*。

  ── [explanation]
  EN | Quite often explanation is not explicitly recognised in documentation; and the idea that things need to be explained is often only faintly expressed. Instead, explanation tends to be scattered in small parcels in other sections.
  旧 | 解释说明常未被明确识别为文档类型；需要解释这一想法，也往往只得到模糊的表达。相反，解释内容倾向于零散地分布在其他章节中。
  新 | 解释说明往往并未在文档中得到明确的承认；事物需要解释这层意思，也往往只是隐约透出。于是，解释说明常常被拆得零零碎碎，散落在其他章节里。

  ── [explanation]
  EN | It's not always easy to write good explanatory material. Where does one start? It's also not clear where to conclude. There is an open-endedness about it that can give the writer too many possibilities.
  旧 | 写出好的解释性材料并不总是容易。从哪里开始？在哪里结束也并不清楚。它具有开放性，可能给作者太多选择。
  新 | 好的解释性材料，写起来并不总是容易。从哪儿起头？到哪里收尾，同样不清楚。它有一种开放性，会让作者面对过多的可能。

  ── [explanation]
  EN | Tutorials, how-to-guides and reference are all clearly defined in their scope by something that is also well-defined: by what you need the user to learn, what task the user needs to achieve, or just by the scope of the machine itself.
  旧 | 教程、实践指南和参考资料的范围都由同样界定清楚的事物明确限定：你需要用户学习什么、用户需要完成什么任务，或设备本身的范围。
  新 | 教程、实践指南和参考资料，其范围都由同样明确的东西界定得清清楚楚：你需要用户学会什么、用户要完成什么任务，或者仅仅是系统本身的范围。

  ── [explanation]
  EN | In the case of explanation, it's useful to have a real or imagined *why* question to serve as a prompt. Otherwise, you simply have to draw some lines that mark out a reasonable area and be satisfied with that.
  旧 | 对于解释说明，最好有一个真实或设想的 *为什么* 问题作为提示。否则，就只能画出界定合理区域的边界，并对此感到满意。
  新 | 就解释说明而言，有一个真实或想象出来的*为什么*问题当引子，会很有用。否则，你就只能划出几条线，圈定一块合理的区域，就此满足。

  ── [explanation]
  EN | When writing explanation you are helping to weave a web of understanding for your readers. **Make connections** to other things, even to things outside the immediate topic, if that helps.
  旧 | 写解释说明时，你在帮助读者编织一张理解之网。若有帮助，便与其他事物建立 **联系**，甚至可联系到眼前主题之外的事物。
  新 | 写解释说明时，你是在帮读者编织一张理解之网。**建立联系**：与其他事物相连，甚至连到眼前主题之外，只要这么做有帮助。

  ── [explanation]
  EN | **Provide background and context in your explanation**: explain *why* things are so - design decisions, historical reasons, technical constraints - draw implications, mention specific examples.
  旧 | **在解释说明中提供背景和语境**：解释事物 *为什么* 如此——设计决策、历史原因、技术约束；推导含义，并提及具体示例。
  新 | **在解释说明中提供背景和语境**：解释事物*为什么*如此——设计决策、历史原因、技术约束——引出其中的含义，举出具体的例子。

  ── [explanation]
  EN | Talk *about* the subject
  旧 | 围绕主题来谈
  新 | *围绕*主题来谈

  ── [explanation]
  EN | why: reasons and justifications
  旧 | 为什么：理由与论证
  新 | 为什么：理由与依据

  ── [explanation]
  EN | Explanation guides are *about* a topic in the sense that they are *around* it. Even the names of your explanation guides should reflect this; you should be able to place an implicit (or even explicit) *about* in front of each title. For example: *About user authentication*, or *About database connection policies*.
  旧 | 解释指南 *关乎* 某个主题，也就是说它们围绕主题展开。解释指南的名称也应反映这一点；应能在每个标题前加上隐含（甚至明确）的“关于”。例如： *关于用户认证* 或 *关于数据库连接策略*。
  新 | 解释指南*关乎*一个主题，也就是说，它*围绕*着主题展开。连解释指南的名字也该体现这一点：每个标题前面，都应该能加上一个隐含的（甚至明确的）*关于*。例如：*关于用户认证*，或*关于数据库连接策略*。

  ── [explanation]
  EN | Opinion might seem like a funny thing to introduce into documentation. The fact is that all human activity and knowledge is invested within opinion, with beliefs and thoughts. The reality of any human creation is rich with opinion, and that needs to be part of any understanding of it.
  旧 | 把观点引入文档可能显得奇怪。但事实是，所有人类活动和知识都蕴含着观点、信念和想法。任何人类创造物的现实都充满观点，理解它就需要将这一点纳入其中。
  新 | 把观点搬进文档，听起来可能有点古怪。可事实是，人类的一切活动与知识，都浸透着观点、信念和想法。任何人类创造物的真实面貌，都满是观点；而要理解它，就必须把这一点也算进去。

  ── [explanation]
  EN | Similarly, any understanding comes from a perspective, a particular stand-point - which means that other perspectives and stand-points exist. **Explanation can and must consider alternatives**, counter-examples or multiple different approaches to the same question.
  旧 | 同样，任何理解都来自某种视角、某个立场——这意味着也存在其他视角和立场。 **解释说明可以且必须考虑替代方案**、反例，或解决同一问题的多种不同方法。
  新 | 同样，任何理解都出自某种视角、某个立场——这就意味着，还存在别的视角和立场。**解释说明能够、也必须考虑替代方案**、反例，或针对同一问题的多种不同做法。

  ── [explanation]
  EN | In explanation, you're not giving instruction or describing facts - you're opening up the topic for consideration. It helps to think of explanation as discussion: discussions can even consider and weigh up contrary *opinions*.
  旧 | 在解释说明中，你不是在给出指令或描述事实，而是在打开主题以供思考。把解释说明视为讨论很有帮助：讨论甚至可以考虑和权衡相反的 *观点*。
  新 | 在解释说明里，你不发指令，也不描述事实——你把主题敞开，供人思考。不妨把解释说明当作讨论：讨论甚至会掂量、权衡相反的*观点*。

  ── [explanation]
  EN | Keep explanation closely bounded
  旧 | 让解释说明保持紧凑边界
  新 | 收紧解释说明的边界

  ── [explanation]
  EN | One risk of explanation is that it tends to absorb other things. The writer, intent on covering the topic, feels the urge to include instruction or technical description related to it. But documentation already has other places for these, and allowing them to creep in interferes with the explanation itself, and removes them from view in the correct place.
  旧 | 解释说明的一个风险是倾向于吞并其他内容。作者为了覆盖主题，会想纳入与之相关的操作指引或技术描述。但文档已有其他位置容纳这些内容，任由它们混入会干扰解释本身，也会让它们在正确的位置中消失。
  新 | 解释说明有一重风险：它容易把别的东西也吞进来。作者一心要覆盖主题，就忍不住要塞进相关的指导内容或技术描述。可这些内容在文档里本来就另有去处；任由它们悄悄溜进来，既干扰解释说明本身，又让它们从本该待的地方消失不见。

  ── [explanation]
  EN | *The reason for x is because historically, y ...*
  旧 | *x 的原因是，在历史上，y……*
  新 | *x 的原因在于，历史上 y……*

  ── [explanation]
  EN | Offer judgements and even opinions where appropriate..
  旧 | 在适当处给出判断，甚至表达观点。
  新 | 在恰当之处给出判断，甚至表达观点。

  ── [explanation]
  EN | Provide context that helps the reader.
  旧 | 提供有助于读者理解的语境。
  新 | 提供能帮到读者的语境。

  ── [explanation]
  EN | *Some users prefer w (because z). This can be a good approach, but...*
  旧 | *有些用户偏好 w（因为 z）。这可能是好方法，但……*
  新 | *有些用户偏好 w（因为 z）。这也许是个好办法，但……*

  ── [explanation]
  EN | Unfold the machinery's internal secrets, to help understand why something does what it does.
  旧 | 揭开设备的内部秘密，帮助理解它为什么会做出相应行为。
  新 | 展开系统内部的秘密，帮人理解某个东西为什么会有那样的表现。

  ── [explanation]
  EN | Analogy from food and cooking
  旧 | 来自食物和烹饪的类比
  新 | 食物与烹饪的类比

  ── [explanation]
  EN | The book doesn't teach how to cook anything. It doesn't contain recipes (except as historical examples) and it isn't a work of reference. Instead, it places food and cooking in the context of history, society, science and technology. It explains for example why we do what we do in the kitchen and how that has changed.
  旧 | 这本书不教人烹饪任何东西，不包含食谱（历史示例除外），也不是参考著作。相反，它把食物和烹饪置于历史、社会、科学和技术的语境中。例如，它解释我们在厨房里为什么这样做，以及这种做法如何变化。
  新 | 这本书不教人做任何菜。它没有食谱（除非作为历史例子），也不是参考书。相反，它把食物与烹饪放进了历史、社会、科学与技术的语境里。比如，它解释我们在厨房里为什么这样做，以及这些做法如何变化。

  ── [explanation]
  EN | It's clearly not a book we would read *while* cooking. We would read when we want to reflect on cooking. It illuminates the subject by taking multiple different perspectives on it, shining light from different angles.
  旧 | 显然，这不是我们会在烹饪 *期间* 阅读的书；而是在想要反思烹饪时才会阅读。它从多种不同的角度审视主题，以不同角度的光线将其照亮。
  新 | 显然，这不是一本我们会在*烹饪当中*读的书。我们读它，是在想要反思烹饪的时候。它从多个不同的视角照亮主题，从不同角度把光照上去。

  ── [explanation]
  EN | After reading a book like *On food and cooking*, our understanding is changed. Our knowledge is richer and deeper. What we have learned may or may not be immediately applicable next time we are doing something in the kitchen, but *it will change how we think about our craft, and will affect our practice*.
  旧 | 读完 *On food and cooking* 这样的书后，我们的理解会改变，知识会更丰富、更深入。下次在厨房做事时，所学内容未必能立即应用，但 *它会改变我们思考技艺的方式，并影响我们的实践*。
  新 | 读完 *On food and cooking* 这样的书之后，我们的理解就变了，知识也更丰富、更深厚。学到的东西，下次在厨房里动手时未必马上用得上；但*它会改变我们对自身技艺的看法，也会影响我们的实践*。
foundations               38 条  改动  18

  ── [foundations]
  EN | Diátaxis is successful because it *works* - both users and creators have a better experience of documentation as a result. It makes sense and it feels right.
  旧 | Diátaxis 之所以成功，是因为它 *有效*：用户和创建者都因此获得更好的文档体验。它合乎道理，也感觉正确。
  新 | Diátaxis 之所以成功，是因为它*有效*——用户和创建者都因此获得了更好的文档体验。它说得通，感觉也对。

  ── [foundations]
  EN | However, that's not enough to be confident in Diátaxis as a theory of documentation. As a theory, it needs to show *why* it works. It needs to show that there is actually some reason why there are exactly four kinds of documentation, not three or five. It needs to demonstrate rigorous thinking and analysis, and that it stands on a sound theoretical foundation.
  旧 | 不过，这还不足以让我们确信 Diátaxis 是一套文档理论。作为理论，它需要说明自己 *为什么* 有效；需要说明文档类型恰好是四种、而不是三种或五种，确有理由；还需要展示严谨的思考和分析，并证明它建立在稳固的理论基础上。
  新 | 然而，这还不足以让我们放心地把 Diátaxis 当作一套文档理论。作为理论，它必须说明自己*为什么*有效。必须说明文档恰好是四类、而非三类或五类，背后确有缘由。还必须展示严谨的思考与分析，证明自己立足于坚实的理论基础。

  ── [foundations]
  EN | Otherwise, it will be just another useful heuristic approach, and the strongest claim we can make for it is that "it seems to work quite well".
  旧 | 否则，它只会是又一种有用的启发式方法，而我们对它最强的主张也只能是“它似乎相当有效”。
  新 | 否则，它不过是又一种有用的启发式方法，而我们能为它作出的最强论断，也不过是“它似乎还挺管用”。

  ── [foundations]
  EN | Diátaxis is based on the principle that documentation must serve the needs of its users. Knowing how to do that means understanding what the needs of users are.
  旧 | Diátaxis 基于这样一项原则：文档必须服务其用户的需求。要做到这一点，就须理解用户需要什么。
  新 | Diátaxis 基于这样一条原则：文档必须服务于其用户的需求。要知道如何做到这一点，就要弄清用户的需求是什么。

  ── [foundations]
  EN | The user whose needs Diátaxis serves is *the practitioner in a domain of skill*. A domain of skill is defined by a craft - the use of a tool or product is a craft. So is an entire discipline or profession. Using a programming language is a craft, as is flying a particular aircraft, or even being a pilot in general.
  旧 | Diátaxis 所服务的用户是 *某一技能领域的实践者*。技能领域由一种技艺界定——使用工具或产品是一种技艺，完整的学科或职业也是。使用一种编程语言是技艺，驾驶某种飞机是技艺，甚至作为飞行员本身也是。
  新 | Diátaxis 所服务的用户，是*某一技能领域的实践者*。技能领域由一门技艺界定——使用一件工具或产品是技艺，一整个学科或职业也是。使用一门编程语言是技艺，驾驶某一型飞机是技艺，甚至泛泛地当一名飞行员，也是技艺。

  ── [foundations]
  EN | Understanding the needs of these users means in turn understanding the essential characteristics of craft or skill.
  旧 | 理解这些用户的需求，进而意味着理解技艺或技能的本质特征。
  新 | 理解这些用户的需求，也就意味着要理解技艺或技能的本质特征。

  ── [foundations]
  EN | A skill or craft or practice contains both **action** (practical knowledge, knowing *how*, what we do) and **cognition** (theoretical knowledge, knowing *that*, what we think). The two are completely bound up with each other, but they are counterparts, wholly distinct from each other, two different aspects of the same thing.
  旧 | 一种技能、技艺或实践同时包含 **知（认知）** （理论知识、知道 *什么*、我们所想的事）和 **行（行动）** （实践知识、知道 *如何*、我们所做的事）。二者完全交织，却又互为对应，彼此截然不同，是同一事物的两个不同方面。
  新 | 一门技能、一种技艺或一项实践，都同时包含**行（行动）**（实践知识、知道*怎么做*、我们所做的事）和**知（认知）**（理论知识、知道*是怎么回事*、我们所想的）。二者完全交织在一起，却又互为对应，彼此截然不同，是同一件事的两个不同方面。

  ── [foundations]
  EN | Similarly, the relationship of a practitioner with their practice is that it is something that needs to be both **acquired**, and **applied**. Being "at work" (concerned with applying the skill and knowledge of their craft) and being "at study" (concerned with acquiring them) are once again counterparts, distinct but bound up with each other.
  旧 | 同样，实践者与其技艺的关系也有 **学（习得）** 与 **用（应用）** 两个方面。“处于学习中”（关注习得技艺的技能和知识）与“处于工作中”（关注应用它们）同样互为对应，既不同又交织。
  新 | 同样，实践者与自己的实践之间也有双重关系：既需要**习得（学）**，也需要**应用（用）**。“处于工作状态”（关注的是应用自己技艺的技能和知识）与“处于学习状态”（关注的是习得它们）同样互为对应，既彼此区分，又相互交织。

  ── [foundations]
  EN | This gives us two dimensions of skill, that we can lay out on a map - a map of the territory of craft:
  旧 | 这给出了技能的两个维度——“知与行”和“学与用”，可将其铺陈在一张地图上——一张技艺领域的地图：
  新 | 这样，我们便得到技能的两个维度，可以把它们铺陈在一张地图上——一张技艺领域的地图：

  ── [foundations]
  EN | The territory of craft as a two-dimensional map
  旧 | 以知与行、学与用两个维度表示的技艺领域
  新 | 以二维地图呈现的技艺领域

  ── [foundations]
  EN | This is a *complete* map. There are only two dimensions, and they don't just cover the entire territory, they define it. This is why there are necessarily four quarters to it, and there could not be three, or five. It is not an arbitrary number.
  旧 | 这是一张 *完整的* 地图。它只有两个维度，二者不仅覆盖整个领域，还定义了该领域。因此它必然有四个象限，不可能是三个或五个；这不是任意的数字。
  新 | 这是一张*完整的*地图。维度只有两个，而这两个维度不仅覆盖整个领域，还界定了这个领域。因此它必然有四个象限，不可能是三个，也不可能是五个。这个数字不是随意定下的。

  ── [foundations]
  EN | It also shows us the *qualities* of craft that define each of them. When the idea that documentation must serve the needs of craft is applied to this map, it reveals in turn what documentation must be and do to fulfil those obligations - in four distinct ways.
  旧 | 它还展示了定义各象限的技艺 *特质*。当把“文档必须服务技艺的需求”这一理念应用到这张地图时，它进而揭示文档为履行这些责任必须成为什么、做什么——以四种截然不同的方式。
  新 | 它还让我们看到界定每一个象限的技艺*品质*。把“文档必须服务于技艺的需求”这一理念放到这张地图上，就会进而揭示出：为履行这些义务，文档必须成为什么、必须做什么——而且是四种截然不同的方式。

  ── [foundations]
  EN | The map of the territory of craft is what gives us the familiar Diátaxis map of documentation. The map is in effect an answer to the question: what must documentation do to align with these qualities of skill, and to what need is it oriented in each case?
  旧 | 技艺领域地图正是我们熟悉的 Diátaxis 文档地图的来源。实际上，这张地图回答的是：文档必须做什么，才能与这些技能特质相一致；在每种情形中，它面向的是哪一种需求？
  新 | 技艺领域的地图，正是我们熟悉的 Diátaxis 文档地图的来源。实际上，这张地图回答的是这样一个问题：文档必须做什么，才能与这些技能的品质相契合；而在每一种情形下，它面向的又是哪一种需求？

  ── [foundations]
  EN | We can see how the map of documentation addresses *needs* across those two dimensions, each need also defined by the characteristics of its quarter of the map.
  旧 | 可以看到，文档地图如何在两个维度上回应 *需求*，每种需求也由所在地图象限的特征界定。
  新 | 我们可以看到，文档地图如何在那两个维度上回应*需求*；而每一种需求，也由它所在象限的特征来界定。

  ── [foundations]
  EN | acquires their craft
  旧 | 习得技艺（学）
  新 | 习得（学）技艺

  ── [foundations]
  EN | applies their craft
  旧 | 应用技艺（用）
  新 | 应用（用）技艺

  ── [foundations]
  EN | The Diátaxis map of documentation is a memorable and approachable idea. But, a map is only reliable if it adequately describes a reality. Diátaxis is underpinned by a systematic description and analysis of generalised **user needs**.
  旧 | Diátaxis 文档地图是一个易于记忆和理解的概念。但地图唯有充分描述现实才可靠。Diátaxis 以对一般化 **用户需求** 的系统描述和分析为基础。
  新 | Diátaxis 文档地图是一个好记、易懂的概念。但地图唯有充分描述现实，才算可靠。Diátaxis 的根基，是对一般化**用户需求**的系统描述与分析。

  ── [foundations]
  EN | This is why the tutorials, how-to guides, reference and explanation of Diátaxis are a complete enumeration of the types of documentation that serve practitioners in a craft. This is why there are four and only four types of documentation. There is simply no other territory to cover.
  旧 | 这就是为什么 Diátaxis 的教程、实践指南、参考资料和解释说明，完整枚举了服务某种技艺实践者的文档类型；这就是为什么文档有且仅有四类。没有其他领域需要覆盖。
  新 | 正因如此，Diátaxis 的教程、实践指南、参考资料和解释说明，才完整地列举了为某种技艺的实践者服务的文档类型。正因如此，文档有且仅有四类。除此之外，根本没有别的领域需要覆盖。
how-to-guides             70 条  改动  64

  ── [how-to-guides]
  EN | How-to guides are **directions** that guide the reader through a problem or towards a result. How-to guides are **goal-oriented**.
  旧 | 实践指南是 **方向指引**，引导读者解决问题或走向结果。实践指南 **以目标为导向**。
  新 | 实践指南是**方向指引**，引导读者解决问题、走向结果。实践指南**以目标为导向**。

  ── [how-to-guides]
  EN | A how-to guide helps the user get something done, correctly and safely; it guides the user's *action*.
  旧 | 实践指南帮助用户正确且安全地完成某项任务；它引导用户的行动，属于 **行**。
  新 | 实践指南帮助用户正确、安全地完成一件事；它引导用户的*行动（行）*。

  ── [how-to-guides]
  EN | It's concerned with *work* - navigating from one side to the other of a real-world problem-field.
  旧 | 它关注 *工作* ——从现实问题领域的一侧导航到另一侧。
  新 | 它关乎*用（应用）*——从现实问题领域的一头走到另一头。

  ── [how-to-guides]
  EN | How-to guides - task oriented, practical steps, that serve our work
  旧 | 实践指南——以任务为导向，通过实际操作步骤（行）服务于技能应用（用）的指南
  新 | 实践指南——面向任务，给出实操步骤，服务于我们的工作（用）

  ── [how-to-guides]
  EN | Examples could be: *how to calibrate the radar array*; *how to use fixtures in pytest*; *how to configure reconnection back-off policies*. On the other hand, *how to build a web application* is not - that's not addressing a specific goal or problem, it's a vastly open-ended sphere of skill.
  旧 | 示例包括： *如何校准雷达阵列*； *如何在 pytest 中使用夹具*； *如何配置重连退避策略*。另一方面， *如何构建 Web 应用程序* 则不是——它并未针对特定目标或问题，而是属于一个极其开放的技能领域。
  新 | 例子可以是：*如何校准雷达阵列*；*如何在 pytest 中使用夹具*；*如何配置重连退避策略*。反过来，*如何构建 Web 应用*就不算——它没有针对具体的目标或问题，而是一片边界极其开放的技能领域。

  ── [how-to-guides]
  EN | How-to guides matter not just because users need to be able to accomplish things: the list of how-to guides in your documentation helps frame the picture of what your product can actually *do*. A rich list of how-to guides is an encouraging suggestion of a product's capabilities.
  旧 | 实践指南之所以重要，不仅是因为用户需要能够完成任务：你的文档中的实践指南列表有助于勾勒产品实际能 *做什么* 的图景。一份丰富的实践指南清单，是对产品能力的鼓舞人心的展示。
  新 | 实践指南之所以重要，不仅因为用户需要办成事情：文档里的实践指南清单，能帮人勾勒出你的产品实际上能*做什么*。一份丰富的实践指南清单，本身就在有力地暗示这个产品能做什么。

  ── [how-to-guides]
  EN | Well-written how-to guides that address the right questions are likely to be the most-read sections of your documentation.
  旧 | 写得好的、解答正确问题的实践指南，很可能是你文档中被阅读最多的部分。
  新 | 写得好、又回答了正确问题的实践指南，很可能成为你文档里被读得最多的部分。

  ── [how-to-guides]
  EN | **How-to guides must be written from the perspective of the user, not of the machinery.** A how-to guide represents something that someone needs to get done. It's defined in other words by the needs of a user. Every how-to guide should answer to a human project, in other words. It should show what the human needs to do, with the tools at hand, to obtain the result they need.
  旧 | **实践指南必须从用户而非机器的角度来撰写**。实践指南代表某人需要完成的事情，换言之，它由用户需求定义。每一份实践指南都应回应人的实际任务，展示用户如何利用手头工具取得所需结果。
  新 | **实践指南必须从用户的角度写，而不是从系统的角度写**。实践指南代表的是某人需要完成的一件事，换言之，它由用户的需求来定义。每一份实践指南都应当回应人的一个项目。它要说明：为了拿到自己需要的结果，这个人用手头的工具该做什么。

  ── [how-to-guides]
  EN | This is in strong contrast to common pattern for how-to guides that often prevails, in which how-to guides are defined by operations that can be performed with a tool or system. The problem with this latter pattern is that it offers little value to the user; it is not addressed to any need the user has. Instead, it's focused on the tool, on taking the machinery through its motions.
  旧 | 这与一种常见且往往占主导地位的模式形成鲜明对比：按照工具或系统可执行的操作来定义实践指南。后一种模式的问题是，它对用户价值有限，没有回应用户的任何需求；它关注的是工具本身，只是让设备机械地完成动作。
  新 | 这与一种常见且往往占上风的模式形成鲜明对照：按工具或系统能做的操作来定义实践指南。后一种模式的问题在于，它对用户几乎没有价值，没有回应到用户的任何需求。它眼里只有工具，只是让系统空走一遍流程。

  ── [how-to-guides]
  EN | This is fundamentally a distinction of *meaningfulness*. Meaning is given by purpose and need. There is no purpose or need in the functionality of a machine. It is merely a series of causes and effects, inputs and outputs.
  旧 | 这本质上是 **是否有意义** 的区别。意义由目的和需求赋予；机器的功能本身没有目的或需求，只是一系列因果、输入和输出。
  新 | 这归根到底是一个*是否有意义*的区别。意义由目的和需求赋予。机器的功能里没有目的，也没有需求，它只是一连串因与果、输入与输出。

  ── [how-to-guides]
  EN | Consider:
  旧 | 请考虑：
  新 | 试看：

  ── [how-to-guides]
  EN | "To shut off the flow of water, turn the tap clockwise."
  旧 | “要切断水流，顺时针旋转水龙头。”
  新 | “要关掉水流，就把水龙头顺时针拧。”

  ── [how-to-guides]
  EN | "To deploy the desired database configuration, select the appropriate options and press **Deploy**."
  旧 | “要部署所需的数据库配置，请选择适当选项并按 **Deploy（部署）**。”
  新 | “要部署所需的数据库配置，就选好相应选项，按**Deploy**。”

  ── [how-to-guides]
  EN | We really do not need to be informed that we turn on a device using the power switch, but it is shocking how often how-to guides in software documentation are written at this level.
  旧 | 我们确实不需要别人告诉我们要用电源开关启动设备，但软件文档中的实践指南竟如此频繁地停留在这一层面，令人震惊。
  新 | 我们实在不需要别人来告诉我们：用电源开关就能打开设备。可软件文档里的实践指南，竟常常停留在这个层次，令人震惊。

  ── [how-to-guides]
  EN | The examples above *look* like examples of guidance, but they are not.
  旧 | 上面的例子 *看起来* 像是指导示例，但它们并不是。
  新 | 上面这些例子*看起来*像在指导，其实不是。

  ── [how-to-guides]
  EN | They represent mostly useless information that anyone with basic competence - anyone who is working in this domain - should be expected to know. Between them, standardised interfaces and generally-expected knowledge should make it quite clear what effect most actions will have.
  旧 | 它们大多代表了对该领域具备基础能力的任何人——即任何在该领域工作的人——都应知晓的无用的信息。标准化的接口和普遍预期的知识应能清楚地表明大多数行动会产生何种影响。
  新 | 它们大多是无用信息，凡是具备基本能力的人——也就是任何在这个领域里做事的人——都理应知道。何况，标准化的界面加上普遍共知的知识，两者合起来，本应让大多数操作的效果一清二楚。

  ── [how-to-guides]
  EN | Secondly, they are disconnected from purpose. What the user needs to know might be things like:
  旧 | 其次，它们与目的脱节。用户需要知道的内容可能包括：
  新 | 其次，它们与目的脱节。用户真正需要知道的，可能是这类事情：

  ── [how-to-guides]
  EN | how much water to run, and how vigorously to run it, for a certain purpose
  旧 | 为了特定目的，需输送多少水以及以何种力度输送
  新 | 为着某个目的，水要放多少，要放多急

  ── [how-to-guides]
  EN | what database configuration options align with particular real-world needs
  旧 | 哪些数据库配置选项符合特定的现实需求
  新 | 哪些数据库配置选项，对应着现实中哪些具体的需要

  ── [how-to-guides]
  EN | How-to guides are about goals, projects and problems, not about tools.
  旧 | 实践指南关注的是目标、项目和问题，而非工具。
  新 | 实践指南讲的是目标、项目和问题，不是工具。

  ── [how-to-guides]
  EN | Tools appear in how-to guides as incidental bit-players, the means to the user's end. Sometimes of course, a particular end is closely aligned with a particular tool or part of the system, and then you will find that a how-to guide indeed concentrates on that. Just as often, a how-to guide will cut across different tools or parts of a system, joining them up together in a series of activities defined by something a human being needs to get done. In either case, it is that project that defines what a how-to guide must cover.
  旧 | 在实践指南中，工具仅作为顺带出现的配角，是达成用户目标的手段。当然，有时某个特定目标与特定工具或系统的一部分紧密相关，此时实践指南确实会聚焦于此；同样经常发生的情况是，实践指南跨越不同的工具或系统部分，将它们在一系列活动中串联起来，这些活动由人类需要完成的任务所定义。无论哪种情况，都是该项目决定了实践指南必须涵盖的内容。
  新 | 在实践指南里，工具只是顺带出场的配角，是用户达成目的的手段。当然，有时某个目的与某个工具或系统的某一部分紧密相关，这时实践指南确实会集中写它。但同样常见的是，实践指南横跨不同的工具或系统的不同部分，把它们串进一系列活动里，而这一系列活动，是由人需要完成的一个项目来定义的。无论哪种情况，实践指南必须涵盖什么，都是由那个项目决定的。

  ── [how-to-guides]
  EN | **How-to guides are wholly distinct from tutorials**. They are often confused, but the user needs that they serve are quite different. Conflating them is at the root of many difficulties that afflict documentation. See :ref:`tutorials-how-to` for a discussion of this distinction.
  旧 | **实践指南与教程截然不同**。二者常被混淆，但它们服务的用户需求完全不同。将两者混为一谈，是许多文档问题的根源。关于这一区别的讨论，请参阅 :ref:`tutorials-how-to`。
  新 | **实践指南与教程截然不同**。二者常被混为一谈，但它们所服务的用户需求相去甚远。把它们搅在一起，是许多困扰文档的难题的根源。关于这一区别的讨论，见 :ref:`tutorials-how-to`。

  ── [how-to-guides]
  EN | In another confusion, how-to guides are often construed merely as procedural guides. But solving a problem or accomplishing a task cannot always be reduced to a procedure. Real-world problems do not always offer themselves up to linear solutions. The sequences of action in a how-to guide sometimes need to fork and overlap, and they have multiple entry and exit-points. Often, a how-to guide will need the user to rely on their judgement in applying the guidance it can provide.
  旧 | 另一种混淆在于，人们常把实践指南仅当作按部就班的流程指引。然而，解决问题或完成一项任务并不总能简化为线性流程。现实世界的问题往往不会自动呈现线性解法。实践指南中的行动序列有时需要分支和重叠，且具备多个入口点和出口点。通常情况下，实践指南需要用户依据自身判断来应用其所提供的指引。
  新 | 另一种混淆，是把实践指南仅仅看成操作流程指南。可是解决问题、完成任务，并非总能化简成一套流程。现实中的问题，也不总能顺着一条直线解决。实践指南里的行动步骤有时需要分叉、需要交叠，还有多个入口和出口。很多时候，实践指南还得让用户自己拿主意，来运用它所能给出的指引。

  ── [how-to-guides]
  EN | A how to-guide is concerned with work - a task or problem, with a practical goal. *Maintain focus on that goal*.
  旧 | 实践指南关注的是工作——具有实际目标的任务或问题。 **始终聚焦于该目标**。
  新 | 实践指南关乎工作——一项有实际目标的任务或问题。*始终盯住那个目标*。

  ── [how-to-guides]
  EN | focused on tasks or problems
  旧 | 专注于任务或问题
  新 | 着眼于任务或问题

  ── [how-to-guides]
  EN | assume the user knows what they want to achieve
  旧 | 假定用户清楚自己的目标
  新 | 假定用户清楚自己想达成什么

  ── [how-to-guides]
  EN | action and only action
  旧 | 只讲行动，不谈其他
  新 | 行动，只有行动

  ── [how-to-guides]
  EN | no digression, explanation, teaching
  旧 | 不旁逸斜出，不做解释说明，不进行教学
  新 | 不跑题，不解释，不教学

  ── [how-to-guides]
  EN | Anything else that's added distracts both you and the user and dilutes the useful power of the guide. Typically, the temptations are to explain or to provide reference for completeness. Neither of these are part of guiding the user in their work. They get in the way of the action; if they're important, link to them.
  旧 | 任何额外添加的内容，都会分散你和用户的注意力，削弱指南的实际作用。通常，诱惑在于为了完整性而进行解释或提供参考资料。这两者都不属于指导用户工作的一部分。它们会妨碍行动；如果它们很重要，请提供链接。
  新 | 凡是多加进来的东西，都会分散你和用户的注意力，冲淡指南的有用之力。常见的诱惑，是为了周全而解释，或者附上参考资料。这两样都不属于在用户的工作中给予引导。它们挡着行动的路；如果确实重要，给出链接就好。

  ── [how-to-guides]
  EN | A how-to guide serves the work of the already-competent user, whom you can assume to know what they want to do, and to be able to follow your instructions correctly.
  旧 | 实践指南服务于已经胜任的用户，你可以假设他们知道自己想做什么，并且能够正确遵循你的指示。
  新 | 实践指南服务的，是已经胜任的用户的工作。你可以假定他们清楚自己想做什么，也能准确照着你的指示做。

  ── [how-to-guides]
  EN | Address real-world complexity
  旧 | 解决现实世界的复杂性
  新 | 应对现实世界的复杂性

  ── [how-to-guides]
  EN | **A how-to guide needs to be adaptable to real-world use-cases**. One that is useless for any purpose except *exactly* the narrow one you have addressed is rarely valuable. You can't address every possible case, so you must find ways to remain open to the range of possibilities, in such a way that the user can adapt your guidance to their needs.
  旧 | **实践指南需要适应现实世界的使用场景**。除了你具体解决的狭窄用途外，对任何目的都无用的指南很少有价值。你无法覆盖所有情况，因此必须设法对各种可能性保持开放，让用户能根据自己的需要来活用你的指引。
  新 | **实践指南要能适应现实中的各种用例**。除了*正好*是你写的那一个狭窄用途之外，别的用途一概用不上——这样的指南很少有价值。你不可能把每种情况都照顾到，所以必须设法对种种可能保持开放，让用户能按自己的需要来变通使用你的指引。

  ── [how-to-guides]
  EN | Omit the unnecessary
  旧 | 省略不必要的内容
  新 | 省去不必要的内容

  ── [how-to-guides]
  EN | In how-to guides, **practical usability is more helpful than completeness.** Whereas a tutorial needs to be a complete, end-to-end guide, a how-to guide does not. It should start and end in some reasonable, meaningful place, and require the reader to join it up to their own work.
  旧 | 在实践指南中， **实用可用性比完整性更有帮助**。虽然教程需要是一份完整的首尾相接的指南，但实践指南则不必如此。它应在某个合理且有意义的地方开始和结束，并要求读者将其与自身工作衔接起来。
  新 | 在实践指南里，**实用的可用性比完整性更有用**。教程得是一份完整、端到端的指南，实践指南不必。它应当起于、止于某个合理而有意义的地方，并且要求读者把它接到自己的工作上去。

  ── [how-to-guides]
  EN | Provide a set of instructions
  旧 | 提供一组指令
  新 | 给出一组指示

  ── [how-to-guides]
  EN | A how-to guide describes an *executable solution* to a real-world problem or task. It's in the form of a contract: if you're facing this situation, then you can work your way through it by taking the steps outlined in this approach. The steps are in the form of *actions*.
  旧 | 实践指南描述了解决现实世界问题或任务的可执行方案。它以契约形式呈现：如果你面临这种情况，那么你可以通过遵循本方法概述的步骤来解决问题。这些步骤以 **行动** 的形式呈现。
  新 | 实践指南描述的，是解决现实问题或任务的*可执行方案*。它像一份契约：如果你正面临这种情形，那么照本办法列出的步骤走，就能走过去。这些步骤以*行动*的形式呈现。

  ── [how-to-guides]
  EN | "Actions" in this context includes physical acts, but also thinking and judgement - solving a problem involves thinking it through. A how-to guide should address how the user thinks as well as what the user does.
  旧 | 此语境下的“行动”不仅包含实际行为，也包括思考与判断——解决问题需要将其想透。实践指南既应关注用户如何思考，也应关注用户如何行动。
  新 | 这里的“行动”既包括实际动作，也包括思考和判断——解决问题离不开把它想透。实践指南既要讲用户怎么做，也要讲用户怎么想。

  ── [how-to-guides]
  EN | Describe a logical sequence
  旧 | 描述一个合乎逻辑的顺序
  新 | 描述合乎逻辑的次序

  ── [how-to-guides]
  EN | The fundamental structure of a how-to guide is a *sequence*. It implies logical ordering in time, that there is a sense and meaning to this particular order.
  旧 | 实践指南的基本结构是一个 *序列*。它意味着时间上的逻辑次序，即这一特定顺序具有意义。
  新 | 实践指南的基本结构是*次序*。它意味着时间上的逻辑先后，意味着这个特定的顺序有其道理和用意。

  ── [how-to-guides]
  EN | In many cases, the ordering is simply imposed by the way things must be (step two requires completion of step one, for example). In this case it's obvious what order your directions should take.
  旧 | 在许多情况下，排序仅仅是由事物的必然方式所决定的（例如，步骤二需要完成步骤一）。在这种情况下，你指令的顺序显而易见。
  新 | 很多时候，顺序就是事物本身的必然（比如第二步要等第一步做完）。这种情况下，你的指引该按什么顺序写，不言自明。

  ── [how-to-guides]
  EN | Sometimes the need is more subtle - it might be possible to *perform* two operations in either order, but if for example one operation helps set up the user's working environment or even their thinking in a way that benefits the other, that's a good reason for putting it first.
  旧 | 有时要求更微妙——两个操作也许可以按任意顺序 *执行*；但若其中一个操作有助于建立用户的工作环境，甚至有助于形成对另一操作有利的思路，就有充分理由将它放在前面。
  新 | 有时这种需要更微妙——两个操作也许*执行*起来谁先谁后都行，但比如其中一个能帮着搭好用户的工作环境，甚至能帮着把思路理顺，从而对另一个有利，那这就是把它放在前面的充分理由。

  ── [how-to-guides]
  EN | At all times, try to ground your sequences in the patterns of the *user's* activities and thinking, in such a way that the guide acquires *flow*: smooth progress.
  旧 | 始终尝试让操作序列立足于 *用户* 的活动和思考模式，使指南获得 *流畅感*：顺畅地推进。
  新 | 时时处处，都要让你的次序扎根于*用户*活动与思考的固有模式，好让指南获得*流畅感*：平顺地向前推进。

  ── [how-to-guides]
  EN | Achieving flow means successfully understanding the user. Paying attention to sense and meaning in ordering requires paying attention to the way human beings think and act, and the needs of someone following directions.
  旧 | 实现流畅感意味着成功理解用户。关注排序中的意义与合理性需要关注人类思考与行为的方式，以及遵循指令者的需求。
  新 | 做到流畅，意味着真正理解用户。要在排序上讲求情理，就得留意人如何思考和行动，留意要照着指示做事的人需要什么。

  ── [how-to-guides]
  EN | Again, this can be somewhat obvious: a workflow that has the user repeatedly switching between contexts and tools is clearly clumsy and inefficient. But you should look more deeply than this. What are you asking the user to think about, and how will their thinking flow from subject to subject during their work? How long do you require the user to hold thoughts open before they can be resolved in action? If you require the user to jump back to earlier concerns, is this necessary or avoidable?
  旧 | 同样，这有时显而易见：让用户在多个上下文和工具间反复切换的工作流程显然笨拙且效率低下。但你要看得更深入。你在要求用户思考什么？在工作中，他们的思绪如何从一个主题流向另一个？你让用户把尚未落地的念头悬多久，之后才能在行动中落实？如果你要求用户回头处理更早的顾虑，这有必要吗，还是可以避免？
  新 | 这同样有些显而易见：让用户在多个情境和工具之间反复切换的工作流程，显然笨拙、低效。但你要看得比这更深。你让用户想的是什么？工作中，他们的思维怎样从一个主题流畅地流向另一个主题？你得让用户把一个念头悬多久，才能在行动中落实？你让用户回头去顾先前的事，这是必要的，还是可以避免的？

  ── [how-to-guides]
  EN | A how-to guide is concerned not just with logical ordering in time, but action taking place in time. Action, and a guide to it, has pace and rhythm. Badly-judged pace or disrupted rhythm are both damaging to flow.
  旧 | 实践指南不仅关乎时间上的逻辑顺序，更关乎行动在时间中的展开。行动，以及关于行动的指南，都有各自的节奏与步调。拿捏失当的节奏，或被打断的韵律，都会破坏流畅感。
  新 | 实践指南关乎的不只是时间上的逻辑先后，还有在时间中发生的行动。行动，以及关于行动的指南，有它的步调和节奏。步调失当，或节奏被打乱，都会破坏流畅感。

  ── [how-to-guides]
  EN | At its best, how-to documentation gives the user flow. There is a distinct experience of encountering a guide that appears to *anticipate* the user - the documentation equivalent of a helper who has the tool you were about to reach for, ready to place it in your hand.
  旧 | 实践指南文档做到最好时，能给用户带来流畅感。遇到似乎能 *预判* 用户需求的指南是一种独特的体验——这相当于文档版的助手，拿着你正要伸手去拿的工具，随时准备递到你手中。
  新 | 实践指南做到最好时，会让用户进入流畅状态。碰到一份似乎能*预判*你的指南，是一种独特的体验——就像遇到一个帮手，你正要伸手去够的工具，他已经拿着，随时递到你手里。

  ── [how-to-guides]
  EN | Pay attention to naming
  旧 | 注意命名方式
  新 | 注意命名

  ── [how-to-guides]
  EN | **Choose titles that say exactly what a how-to guide shows.**
  旧 | **选择恰如其分的标题来准确说明实践指南所演示的内容。**
  新 | **标题要准确说出这份实践指南展示的是什么。**

  ── [how-to-guides]
  EN | good: *How to integrate application performance monitoring*
  旧 | 良好： *如何集成应用程序性能监控*
  新 | 好：*如何集成应用性能监控*

  ── [how-to-guides]
  EN | bad: *Integrating application performance monitoring* (maybe the document is about how to decide whether you should, not about how to do it)
  旧 | 不佳： *集成应用程序性能监控* （或许文档讲的是是否应该集成，而非如何操作）
  新 | 不好：*集成应用性能监控*（也许文档讲的是该不该做，而不是怎么做）

  ── [how-to-guides]
  EN | very bad: *Application performance monitoring* (maybe it's about *how* - but maybe it's about *whether*, or even just an explanation of *what* it is)
  旧 | 非常差： *应用程序性能监控* （或许它讲的是 *如何* ——但也可能是讲 *是否*，甚至只是对 *是什么* 的解释）
  新 | 极差：*应用性能监控*（也许它讲的是*如何*，但也可能是*是否*，甚至只是在解释它*是什么*）

  ── [how-to-guides]
  EN | Note that search engines appreciate good titles just as much as humans do.
  旧 | 请注意，搜索引擎与人类一样也偏爱好的标题。
  新 | 注意，搜索引擎和人一样，都看重好标题。

  ── [how-to-guides]
  EN | *This guide shows you how to...*
  旧 | *本指南向你展示如何……*
  新 | *本指南教你如何……*

  ── [how-to-guides]
  EN | Describe clearly the problem or task that the guide shows the user how to solve.
  旧 | 清晰描述该实践指南所示用户要解决的问题或任务。
  新 | 清楚说明这份指南要教用户解决的是什么问题或任务。

  ── [how-to-guides]
  EN | *If you want x, do y. To achieve w, do z.*
  旧 | *如果你想要 x，请执行 y；若要实现 w，请执行 z。*
  新 | *如果你想要 x，就做 y。要达成 w，就做 z。*

  ── [how-to-guides]
  EN | Use conditional imperatives.
  旧 | 使用条件祈使句。
  新 | 用条件式祈使句。

  ── [how-to-guides]
  EN | *Refer to the x reference guide for a full list of options.*
  旧 | *有关选项的完整列表，请参阅 x 参考资料。*
  新 | *选项的完整清单，见 x 参考指南。*

  ── [how-to-guides]
  EN | Don't pollute your practical how-to guide with every possible thing the user might do related to x.
  旧 | 不要把你撰写的实用实践指南，塞满用户围绕 x 可能做的每一件事，以免把它搞得杂乱无章。
  新 | 别把用户围绕 x 可能做的每一件事，全塞进你的实践指南。

  ── [how-to-guides]
  EN | Applied to food and cooking
  旧 | 应用于食品与烹饪
  新 | 套用在饮食烹饪上

  ── [how-to-guides]
  EN | Consider a recipe, an excellent model for a how-to guide. A recipe clearly defines what will be achieved by following it, and **addresses a specific question** (*How do I make...?* or *What can I make with...?*).
  旧 | 考虑食谱，它是实践指南的绝佳范例。食谱清晰地定义了遵循该指南后达成的成果，并 **解答了一个特定问题** （ *我该如何制作……？* 或 *用……我能做什么？*）。
  新 | 想一想食谱——实践指南的绝佳范本。食谱清楚说明照着做能做成什么，并且**回答一个具体的问题**（*我要怎么做……？*还是*我能拿……做什么？*）。

  ── [how-to-guides]
  EN | A recipe contains a list of ingredients and a list of steps.
  旧 | 食谱包含一份配料清单和一份步骤清单。
  新 | 一份食谱包含一份配料清单和一份步骤清单。

  ── [how-to-guides]
  EN | It's not the responsibility of a recipe to *teach* you how to make something. A professional chef who has made exactly the same thing multiple times before may still follow a recipe - even if they *created* the recipe themselves - to ensure that they do it correctly.
  旧 | 食谱的责任并非 *教授* 你如何制作某物。一位多次做过完全相同菜肴的专业厨师，也仍会照着食谱做——哪怕这食谱就是他本人写的——以确保做对。
  新 | 食谱的职责不是*教*你怎么做一道菜。一位专业厨师，哪怕同一道菜已经做过很多遍，也可能仍旧照着食谱做——哪怕这食谱是他自己*写*的——就为确保做得没错。

  ── [how-to-guides]
  EN | Even following a recipe **requires at least basic competence**. Someone who has never cooked before should not be expected to follow a recipe with success, so a recipe is not a substitute for a cooking lesson.
  旧 | 即便遵循食谱 **也至少需要基本能力**。从未做过饭的人，不应指望单靠一份食谱就能做成功，因此食谱不能替代烹饪课。
  新 | 即便是照着食谱做，**也至少要有基本的能力**。从没下过厨的人，别指望他能照着食谱做成，所以食谱替代不了一堂烹饪课。

  ── [how-to-guides]
  EN | Someone who expected to be provided with a recipe, and is given instead a cooking lesson, will be disappointed and annoyed. Similarly, while it's interesting to read about the context or history of a particular dish, the one time you don't want to be faced with that is while you are in the middle of trying to make it. A good recipe follows a well-established format, that excludes both teaching and discussion, and focuses only on **how** to make the dish concerned.
  旧 | 若某人期望获得食谱却得到烹饪课程，难免失望恼怒。同理，虽然了解特定菜肴的背景或历史颇有趣味，但你最不希望面对这些的时候正是亲手制作其间。优质食谱遵循既定的标准格式，排除教学与讨论，只聚焦于 **如何** 制作相应菜肴。
  新 | 一个人想要食谱，得到的却是一堂烹饪课，他会失望，会恼火。同样，读读某道菜的背景或来历固然有趣，可你唯一不想碰上这些的时候，正是你正忙着做这道菜的时候。好的食谱遵循一种成熟定型的格式，既不讲教学，也不作讨论，只专注于**如何**做这道菜。
how-to-use-diataxis       34 条  改动  32

  ── [how-to-use-diataxis]
  EN | Diátaxis as a guide to work
  旧 | 将 Diátaxis 用作工作指南
  新 | Diátaxis 作为工作指南

  ── [how-to-use-diataxis]
  EN | As well as providing a guide to documentation content, Diátaxis is also a guide to documentation process and execution.
  旧 | Diátaxis 不仅提供文档内容方面的指引，也指导文档的流程与执行。
  新 | Diátaxis 不仅是文档内容的指南，也是文档工作方式与执行方式的指南。

  ── [how-to-use-diataxis]
  EN | Most people who work on technical documentation must make decisions about how to work, as they work. In some contexts, documentation must be delivered once, complete and in its final state, but it's more usual that it's an on-going project, for example developed alongside a product that itself evolves and develops. It's also the experience of many people who work on documentation to find themselves responsible for improving or even remediating a body of work.
  旧 | 大多数技术文档工作者都必须在工作过程中决定如何开展工作。在某些语境中，文档必须一次性交付，完整且处于最终状态；但更常见的是，它是持续进行的项目，例如与不断演变发展的产品一起开发。许多文档工作者也会发现，自己负责改进甚至整治一整套文档。
  新 | 大多数做技术文档的人，都得一边做事，一边决定该怎么做。在有些场合，文档只交付一次，交出去时就得是完整、定稿的状态；但更常见的情况是，文档是个一直在推进的项目，比如与一个自身也不断演进、发展的产品同行。许多做文档的人也有这样的体会：发现自己要负责改进、甚至补救一整套文档。

  ── [how-to-use-diataxis]
  EN | Diátaxis provides an approach to work that runs counter to much of the accepted wisdom in documentation. In particular, it discourages planning and top-down workflows, preferring instead small, responsive iterations from which overall patterns emerge.
  旧 | Diátaxis 提供的工作方法有悖于文档领域许多被普遍接受的智慧。尤其是，它不鼓励规划和自上而下的工作流，转而偏好小步、灵活应变的迭代，让整体模式从中自然涌现。
  新 | Diátaxis 给出的工作方法，与文档领域许多公认的智慧背道而驰。它尤其不鼓励规划和自上而下的工作流，而更青睐注重响应的小步迭代，让整体格局从中浮现。

  ── [how-to-use-diataxis]
  EN | Use Diátaxis as a guide, not a plan
  旧 | 将 Diátaxis 用作指南，而非计划
  新 | 把 Diátaxis 当指南，而非计划

  ── [how-to-use-diataxis]
  EN | Diátaxis describes a complete picture of documentation. However the structure it proposes is not intended to be a **plan**, something you must complete in your documentation. It's a **guide**, a map to help you check that you're in the right place and going in the right directions.
  旧 | Diátaxis 描绘了文档的完整图景，但其提出的结构并非必须在文档中完成的 **计划**。它是一份 **指南**，一张帮助你确认自己身处正确位置、朝正确方向前进的地图。
  新 | Diátaxis 描绘了文档的完整图景。不过，它提出的结构，本意并不是一份你必须在文档中完成的**计划**。它是一份**指南**，一张地图，帮你确认自己身在正确的位置、正朝着正确的方向。

  ── [how-to-use-diataxis]
  EN | The point of Diátaxis is to give you a way to think about and understand your documentation, so that you can make better sense of what it's doing and what you're trying to do with it. It provides tools that help assess it, identify where its problems lie, and judge what you can do to improve it.
  旧 | Diátaxis 的要点是让你能思考和理解自己的文档，从而更好地理解它在做什么，以及你试图借它完成什么。它提供工具来帮助评估文档、定位问题，并判断可以怎样改进。
  新 | Diátaxis 的用意，是给你一种方式，去思考和理解自己的文档，从而更明白它在做什么、你想拿它做什么。它还提供工具，帮你评估文档、找出问题所在、判断你能做些什么来改进。

  ── [how-to-use-diataxis]
  EN | Don't worry about structure
  旧 | 不必忧虑结构
  新 | 别为结构操心

  ── [how-to-use-diataxis]
  EN | Although structure is key to documentation, **using Diátaxis means not spending energy trying to get its structure correct**.
  旧 | 尽管结构是文档的关键， **使用 Diátaxis 意味着不必耗费精力试图让其结构正确。**
  新 | 尽管结构对文档至关重要，但**用 Diátaxis，就意味着不必耗费精力去把它的结构弄对**。

  ── [how-to-use-diataxis]
  EN | If you continue to follow the prompts that Diátaxis provides, eventually your documentation will assume the Diátaxis structure - but it will have assumed that shape *because* it has been improved. It's not the other way round, that the structure must be imposed upon documentation to improve it.
  旧 | 只要持续遵循 Diátaxis 的提示，文档最终会呈现 Diátaxis 的结构——但它获得这种形状是 *因为* 已被改进，而不是反过来，必须先将结构强加给文档才能改进它。
  新 | 只要一直跟着 Diátaxis 的提示走，你的文档最终会呈现 Diátaxis 的结构——但它是*因为*被改进了，才长成那个形状。而不是反过来，必须先给文档强加结构，才能改进它。

  ── [how-to-use-diataxis]
  EN | Getting started with Diátaxis does not require you to think about dividing up your documentation into four sections. **It certainly does not mean that you should create empty structures for tutorials/howto guides/reference/explanation with nothing in them.** Don't do that. It's horrible.
  旧 | 开始使用 Diátaxis，并不需要考虑把文档分成四个部分。 **当然更不意味着应先为教程、实践指南、参考资料和解释说明创建没有任何内容的空结构。** 不要这样做，太糟糕了。
  新 | 开始使用 Diátaxis，并不需要你去考虑把文档分成四个部分。**当然，这更不意味着你该为教程、实践指南、参考资料和解释说明搭起空架子，里面什么都没有。**别这么做，那很糟糕。

  ── [how-to-use-diataxis]
  EN | Instead, following the workflow described in the next two sections, make changes where you see opportunities for improvement according to Diátaxis principles, so that the documentation starts to take a certain shape. At a certain point, the changes you have made will appear to demand that you move material under a certain Diátaxis heading - and that is how your top-level structure will form. In other words, **Diátaxis changes the structure of your documentation from the inside**.
  旧 | 相反，遵循后两节描述的工作流程，按 Diátaxis 原则在看到改进机会之处进行改动，让文档逐渐形成某种形态。到某一时刻，已作出的改动似乎会要求你把材料移到某个 Diátaxis 标题下——顶层结构便会如此形成。换言之， **Diátaxis 从内部改变文档结构。**
  新 | 相反，照着接下来两节讲的工作流程，按 Diátaxis 的原则，看到哪里可改进，就在哪里动手改，让文档开始显露出某种形态。到某个时候，你做的这些改动仿佛会要求你把材料归到某个 Diátaxis 标题之下——你的顶层结构就是这样形成的。换言之，**Diátaxis 从内部改变你文档的结构**。

  ── [how-to-use-diataxis]
  EN | Work one step at a time
  旧 | 一次推进一步
  新 | 一步一个脚印地做

  ── [how-to-use-diataxis]
  EN | Diátaxis strongly prescribes a structure, but whatever the state of your existing documentation - even if it's a complete mess by any standards - it's always possible to improve it, **iteratively**.
  旧 | Diátaxis 对结构有明确要求；但无论现有文档处于何种状态——即使按任何标准都一团糟——总能通过 **迭代** 加以改进。
  新 | Diátaxis 给结构定下了极严的规矩，但无论你现有的文档是什么状态——哪怕按任何标准看都一团糟——总能**迭代**着把它改好。

  ── [how-to-use-diataxis]
  EN | It's natural to want to complete large tranches of work before you publish them, so that you have something substantial to show each time. Avoid this temptation - every step in the right direction is worth publishing immediately.
  旧 | 人们自然会想先完成大量工作再发布，以便每次都有实质成果可展示。请避免这种诱惑——朝正确方向迈出的每一步，都值得立刻发布。
  新 | 人们自然想先把一大批工作做完再发布，好让每次拿出来的东西都够分量。要忍住这种诱惑——朝正确方向迈出的每一步，都值得立刻发布。

  ── [how-to-use-diataxis]
  EN | Although Diátaxis is intended to provide a big picture of documentation, **don't try to work on the big picture**. It's both unnecessary and unhelpful. Diátaxis is designed to guide small steps; keep taking small steps to arrive where you want to go.
  旧 | 尽管 Diátaxis 意在提供文档的大图景， **不要试图处理大图景本身**。那既不必要也无益。Diátaxis 用于引导小步前进；持续迈出小步，便能抵达想去的地方。
  新 | 尽管 Diátaxis 意在给出文档的大图景，**但不要试图从大图景入手**。那既不必要，也没有益处。Diátaxis 要引导的，正是小步；一直迈小步，就能走到你想去的地方。

  ── [how-to-use-diataxis]
  EN | Just do something
  旧 | 先做点什么
  新 | 动手做点什么

  ── [how-to-use-diataxis]
  EN | If you're tidying up a huge mess, the temptation is to tear it all down and start again. Again, avoid it. As far as improving documentation in-line with Diátaxis goes, it isn't necessary to seek out things to improve. Instead, the best way to apply Diátaxis is as follows:
  旧 | 面对一大摊混乱，容易想将它全部推倒重来。再次提醒，请避免这样做。要按照 Diátaxis改进文档，无需特意寻找要改进的事物；应用 Diátaxis 的最佳方式如下：
  新 | 收拾一大摊烂摊子时，很容易想推倒重来。同样，要忍住。就依照 Diátaxis 改进文档这件事来说，其实不必特意去找可改之处。运用 Diátaxis 的最佳方式如下：

  ── [how-to-use-diataxis]
  EN | **Choose something** - any piece of the documentation. If you don’t already have something that you know you want to put right, don't go looking for outstanding problems. Just look at what you have right in front of you at that moment: the file you’re in, the last page you read - it doesn’t matter. If there isn’t one just choose something, literally at random.
  旧 | **选择某个对象** ——文档中的任意部分。若还没有明确想修正的内容，不要去搜寻遗留问题。只需看此刻眼前已有的内容：当前文件、最后读过的页面——都可以。若实在没有，就随机选一个。
  新 | **挑一样东西**——文档里的任何一块都行。如果你心里还没有什么明确想修正的东西，就别去翻找遗留的问题。只看那一刻眼前有什么：正打开的文件、刚读过的页面——都无所谓。要是手边没有，那就随便挑一样，真的是随手挑。

  ── [how-to-use-diataxis]
  EN | **Assess it**. Next consider this thing critically. Preferably it’s a small thing, nothing bigger than a page - or better, even smaller, a paragraph or a sentence. Challenge it, according to the standards Diátaxis prescribes: *What user need is represented by this? How well does it serve that need? What can be added, moved, removed or changed to serve that need better? Do its language and logic meet the requirements of this mode of documentation?*
  旧 | **评估它。** 接着批判性地思考该对象。最好选小一点的对象，不超过一页；再小一些，一段或一句就更好。根据 Diátaxis 的标准审视它： *它代表何种用户需求？它对该需求服务得如何？可以添加、移动、删除或更改什么，以更好地服务该需求？其语言和逻辑是否符合这种文档形式的要求？*
  新 | **评估它**。接下来，用批判的眼光审视这个东西。最好是个小东西，不超过一页——再小些更好，一段话或一句话就够。然后按 Diátaxis 确立的标准去质疑它：*它代表着什么用户需求？它把这个需求满足得如何？要更好地满足这个需求，可以增加、移动、删除或改动什么？它的语言和逻辑，符合这类文档的要求吗？*

  ── [how-to-use-diataxis]
  EN | **Decide what to do**. Decide, based on your answers to those questions: *What single next action will produce an immediate improvement here?*
  旧 | **决定怎么做。** 根据对这些问题的回答作出决定： *哪一项单独的下一步行动能立即带来改进？*
  新 | **决定做什么**。根据你对这些问题的回答来决定：*哪一项单独的下一步行动，能立刻给这里带来改进？*

  ── [how-to-use-diataxis]
  EN | **Do it**. Complete that next single action, *and consider it completed* - i.e. publish it, or at least commit the change. Don't feel that you need to do anything else to make a worthy improvement.
  旧 | **去做。** 完成那一项单独的下一步行动， *并将其视为已完成* ——即发布它，或至少提交这项改动。无需认为还必须做其他事，才能称得上一次有价值的改进。
  新 | **动手做**。把那单独的下一步行动做完，*并且就当它已经完成*——也就是把它发布出去，或者至少提交这次改动。别以为非得再做点什么，才算得上有价值的改进。

  ── [how-to-use-diataxis]
  EN | And then go back to the beginning of the cycle.
  旧 | 然后回到循环的起点。
  新 | 然后，回到循环的起点。

  ── [how-to-use-diataxis]
  EN | Working like this helps reduce the stress of one of the most paralysing and troublesome aspects of the documentation-writer's work: working out what to do. It keeps work flowing in the right direction, always towards the desired end, without having to expend energies on a plan.
  旧 | 这样工作，有助于减轻文档作者工作里最令人一筹莫展、最麻烦的一环带来的压力：想清楚该做什么。它让工作持续朝正确方向流动，始终指向期望的终点，无需在计划上耗费精力。
  新 | 这样工作，能帮你卸掉一份压力——文档作者最让人无从下手、最麻烦的事情之一，就是想清楚该做什么。它让工作始终朝正确的方向流动，始终奔向想要的终点，而不必在计划上耗费精力。

  ── [how-to-use-diataxis]
  EN | There's a strong urge to work in a cycle of planning and execution in order to work towards results. But it's not the only way, and there are often better ways when working with documentation.
  旧 | 为了取得成果，人们强烈倾向于在计划和执行的循环中工作。但这并非唯一方式；处理文档时，往往有更好的方法。
  新 | 人们总有一种强烈的冲动：为了做出成果，就在计划与执行的循环里工作。但这并非唯一的办法；做文档时，往往还有更好的做法。

  ── [how-to-use-diataxis]
  EN | A good model for documentation is **well-formed organic growth that adapts to external conditions**. Organic growth takes place at the cellular level. The structure of the organism as a whole is guaranteed by the healthy development of cells, according to rules that are appropriate to each kind of cell. It's not the other way round, that a structure is imposed on the organism from above or outside. Good structure develops from within.
  旧 | 文档的一个好模型是 **适应外部条件、良好成形的有机生长**。有机生长发生在细胞层面；整体结构由细胞依其类型适用的规则健康发展来保证。这并非从上方或外部把结构强加给有机体；良好结构从内部发展而来。
  新 | 文档的好模型，是**适应外部条件、良好成形的有机生长**。有机生长发生在细胞层面：细胞按各自适用的规则健康发育，有机体作为整体的结构便有了保证。而不是反过来，从上方或外部把结构强加给有机体。好的结构由内而生。

  ── [how-to-use-diataxis]
  EN | Illustration copyright `Linette Voller <https://linettevoller.com>`_ 2021, reproduced with kind permission.
  旧 | 插图版权归 `Linette Voller <https://linettevoller.com>`_ 所有，2021 年，经许可转载。
  新 | 插图版权归 `Linette Voller <https://linettevoller.com>`_ 所有，2021 年，经慨允转载。

  ── [how-to-use-diataxis]
  EN | It's the same with documentation: by following the principles that Diátaxis provides, your documentation will attain a healthy structure, because its internal components themselves are well-formed - like a living organism, it will have built itself up from the inside-out, one cell at a time.
  旧 | 文档也是如此：遵循 Diátaxis 提供的原则，文档会获得健康的结构，因为其内部组成部分本身良好成形——就像生物体一样，它会从内向外、逐个细胞地构建自己。
  新 | 文档也一样：只要遵循 Diátaxis 提供的原则，你的文档就会长出健康的结构，因为它的内部构件本身都良好成形——就像活的有机体，由内而外、一个细胞一个细胞地把自己搭建起来。

  ── [how-to-use-diataxis]
  EN | Complete, not finished
  旧 | 完整，而非终结
  新 | 完整，而非完成

  ── [how-to-use-diataxis]
  EN | Consider a plant. As a living, growing organism, a plant is **never finished** - it can always develop further, move on to the next stage of growth and maturity. But, at every stage of its development, from seed to a fully-mature tree, it's **always complete** - there's never something missing from it. At any point, it is in a state that is appropriate to its stage of development.
  旧 | 想想一株植物。作为活着且不断生长的有机体，植物 **永远不会终结** ——它始终可以继续发展，进入生长和成熟的下一阶段。但在其从种子到完全成熟大树的每一个发展阶段，它又 **始终是完整的** ——从不缺失什么。在任何时点，它都处于适合其发展阶段的状态。
  新 | 想想一株植物。植物是活着的、不断生长的有机体，**永远不会完成**——它总能继续发展，走向生长与成熟的下一阶段。可是，从一粒种子到一棵完全长成的大树，在它发育的每一个阶段，它又**始终是完整的**——从不缺少什么。在任何时刻，它都处在与自身发展阶段相称的状态。

  ── [how-to-use-diataxis]
  EN | Similarly, documentation is also never finished, because it always has to keep adapting and changing to the product and to users' needs, and can always be developed and improved further.
  旧 | 同样，文档也永远不会终结，因为它总要持续适应产品和用户需求的变化，并且总能被进一步发展和改进。
  新 | 同样，文档也永远不会完成，因为它总得不断适应产品、适应用户需求，随之而变，也总能继续发展、继续改进。

  ── [how-to-use-diataxis]
  EN | However it can always be complete: useful to users, appropriate to its current stage of development, and in a healthy structural state and ready to go on to the next stage.
  旧 | 不过它始终可以是完整的：对用户有用，适合当前的发展阶段，结构健康，并准备好进入下一阶段。
  新 | 不过，它随时都可以是完整的：对用户有用，合乎当前的发展阶段，结构处于健康状态，并已准备好进入下一阶段。
index                     32 条  改动  16

  ── [index]
  EN | Start here
  旧 | 从此开始
  新 | 从这里开始

  ── [index]
  EN | Diátaxis is a widely-adopted, pragmatic and systematic approach to thinking about and creating documentation.
  旧 | Diátaxis 是一种被广泛采用、务实且系统化的文档思考与创建方法。
  新 | Diátaxis 是一种广为采用、务实且系统化的方法，用于思考和创建文档。

  ── [index]
  EN | :doc:`Help translate Diátaxis <translation>` into your language.
  旧 | :doc:`帮助将 Diátaxis 翻译 <translation>` 成你的语言。
  新 | :doc:`帮助把 Diátaxis 翻译成你的语言 <translation>`。

  ── [index]
  EN | It prescribes approaches to content, architecture and form that emerge from a systematic approach to understanding the needs of documentation users.
  旧 | 它为内容、架构和形式提出了相应方法；这些方法源于对文档使用者需求的系统理解。
  新 | 它为内容、架构和形式规定了具体做法，而这些做法源于对文档用户需求的系统理解。

  ── [index]
  EN | Diátaxis identifies four distinct needs, and four corresponding forms of documentation - *tutorials*, *how-to guides*, *technical reference* and *explanation*. It places them in a systematic relationship, and proposes that documentation should itself be organised around the structures of those needs.
  旧 | Diátaxis 识别出四种截然不同的需求，以及与之对应的四种文档形式： *教程*、 *实践指南*、 *技术参考资料* 和 *解释说明*。它将它们置于系统化的关系中，并主张文档本身应围绕这些需求的结构来组织。
  新 | Diátaxis 辨识出四种截然不同的需求，以及与之对应的四种文档形式——*教程*、*实践指南*、*技术参考资料*\ 和\ *解释说明*。它把这些需求与形式置于一种系统性的关系之中，并主张文档本身就该围绕这些需求的结构来组织。

  ── [index]
  EN | *Diátaxis*, from the Ancient Greek δῐᾰ́τᾰξῐς: *dia* ("across") and *taxis* ("arrangement").
  旧 | *Diátaxis* 源自古希腊语 δῐᾰ́τᾰξῐς： *dia* （“横跨”）和 *taxis* （“编排”）。
  新 | *Diátaxis* 源自古希腊语 δῐᾰ́τᾰξῐς：*dia*\ （“横跨”）和 *taxis*\ （“编排”）。

  ── [index]
  EN | Diátaxis solves problems related to documentation *content* (what to write), *style* (how to write it) and *architecture* (how to organise it).
  旧 | Diátaxis 解决与文档 *内容* （写什么）、 *风格* （怎样写）和 *架构* （怎样组织）有关的问题。
  新 | Diátaxis 解决的是与文档\ *内容*\ （写什么）、*风格*\ （怎样写）、*架构*\ （怎样组织）有关的问题。

  ── [index]
  EN | As well as serving the users of documentation, Diátaxis has value for documentation creators and maintainers. It is light-weight, easy to grasp and straightforward to apply. It doesn't impose implementation constraints. It brings an active principle of quality to documentation that helps maintainers think effectively about their own work.
  旧 | Diátaxis 不仅服务文档使用者，也对文档的创建者和维护者有价值。它轻量、易理解、易应用，不会强加实现约束。它为文档带来一项积极的质量原则，帮助维护者有效思考自己的工作。
  新 | Diátaxis 不仅为文档用户服务，对文档的创建者和维护者也有价值。它轻量、易于上手、运用起来也直截了当。它不施加任何实现上的约束。它把一项积极的质量原则带进文档，帮助维护者有效地思考自己的工作。

  ── [index]
  EN | Contents
  旧 | 内容
  新 | 目录

  ── [index]
  EN | The best way to get started with Diátaxis is by applying it after reading a brief primer.
  旧 | 阅读一份简要导读后，将 Diátaxis 应用于实际问题，是开始使用它的最佳方式。
  新 | 上手 Diátaxis 的最好办法，就是先读一份简明入门，再把它用起来。

  ── [index]
  EN | These pages will help make immediate, concrete sense of the approach.
  旧 | 这些页面将帮助你立刻、具体地理解这一方法。
  新 | 这些页面会帮你立刻、具体地领会这套方法。

  ── [index]
  EN | This section explores the theory and principles of Diátaxis more deeply, and sets forth the understanding of needs that underpin it.
  旧 | 本节深入探索 Diátaxis 的理论与原则，并阐明支撑它的需求理解。
  新 | 本节更深入地探讨 Diátaxis 的理论与原则，并阐明作为其根基的需求观。

  ── [index]
  EN | Diátaxis is proven in practice. Its principles have been adopted successfully in hundreds of documentation projects.
  旧 | Diátaxis 已在实践中得到证明；其原则已成功应用于数百个文档项目。
  新 | Diátaxis 已在实践中得到证明。数以百计的文档项目成功采用了它的原则。

  ── [index]
  EN | Diátaxis has allowed us to build a high-quality set of internal documentation that our users love, and our contributors love adding to.
  旧 | Diátaxis 让我们构建了一套高质量的内部文档：用户喜欢阅读，贡献者也乐于持续补充。
  新 | Diátaxis 让我们得以搭建起一套高质量的内部文档：我们的用户喜欢它，我们的贡献者也乐于为它添砖加瓦。

  ── [index]
  EN | At Gatsby we recently reorganized our open-source documentation, and the Diátaxis framework was our go-to resource throughout the project. The four quadrants helped us prioritize the user’s goal for each type of documentation. By restructuring our documentation around the Diátaxis framework, we made it easier for users to discover the resources that they need when they need them.
  旧 | 最近，Gatsby 重组了开源文档，而 Diátaxis 框架是我们在整个项目中首选的参考资源。四个象限帮助我们确定每种文档应优先服务的用户目标。围绕 Diátaxis 框架重构文档后，用户更容易在需要时发现所需资源。
  新 | 最近，我们重组了 Gatsby 的开源文档，而 Diátaxis 框架是我们在整个项目中首选的参考资源。四个象限帮我们确定每种文档应当优先满足的用户目标。围绕 Diátaxis 框架重构文档后，我们让用户在需要的时候更容易找到所需的资源。

  ── [index]
  EN | While redesigning the `Cloudflare developer docs <https://developers.cloudflare.com>`_, Diátaxis became our north star for information architecture. When we weren't sure where a new piece of content should fit in, we'd consult the framework. Our documentation is now clearer than it's ever been, both for readers and contributors.
  旧 | 在重新设计 `Cloudflare 开发者文档 <https://developers.cloudflare.com>`_ 时，Diátaxis 成为我们信息架构的北极星。每当不确定一项新内容应放在何处，我们就查阅这一框架。如今，无论对读者还是贡献者，文档都比以往清晰。
  新 | 在重新设计 `Cloudflare 开发者文档 <https://developers.cloudflare.com>`_ 时，Diátaxis 成了我们信息架构的北极星。每当拿不准一项新内容该放在哪里，我们就去查这套框架。如今，我们的文档比以往任何时候都更清晰，无论对读者还是贡献者都是如此。
map                       73 条  改动  34

  ── [map]
  EN | One reason Diátaxis is effective as a guide to organising documentation is that it describes a **two-dimensional structure**, rather than a *list*.
  旧 | Diátaxis 作为组织文档的指南之所以有效，一个原因是它描述的是 **二维结构**，而非一份 *列表*：这两个维度是“知与行”和“学与用”。
  新 | Diátaxis 作为组织文档的指南之所以有效，一个原因在于它描述的是**二维结构**，而非一份*列表*。

  ── [map]
  EN | It specifies its types of documentation in such a way that the structure naturally helps guide and shape the material it contains.
  旧 | 它以这样的方式规定文档类型：结构自然有助于引导和塑造其中包含的材料。
  新 | 它规定文档类型的方式，让这套结构能自然而然地引导并塑造它所容纳的材料。

  ── [map]
  EN | As a map, it places the different forms of documentation into relationships with each other. Each one occupies a space in the mental territory it outlines, and the boundaries between them highlight their distinctions.
  旧 | 作为地图，它将不同形式的文档置于彼此关联中。每一种都占据其勾勒出的心理领域中的一块空间，它们之间的边界凸显各自的区别。
  新 | 作为地图，它让不同形式的文档彼此建立关联。每一种都在它勾勒出的心智疆域中占据一方，而它们之间的边界，凸显出彼此的区别。

  ── [map]
  EN | When documentation fails to attain a good structure, it's rarely just a problem of structure (though it's bad enough that it makes it harder to use and maintain). Architectural faults infect and undermine content too.
  旧 | 文档未能形成良好结构时，很少只是结构问题（尽管这已经足以使使用和维护更困难）。架构缺陷也会侵蚀并削弱内容。
  新 | 文档没能形成良好的结构时，问题很少只出在结构上（可单是这一点，就已经让文档更难使用、更难维护）。架构上的缺陷同样会侵染、削弱内容。

  ── [map]
  EN | In the absence of a clear, generalised documentation architecture, documentation creators will often try to structure their work around features of a product.
  旧 | 缺乏清晰、通用的文档架构时，文档创建者往往会尝试围绕产品特性来组织工作。
  新 | 缺乏清晰、通用的文档架构时，文档创建者往往会试着围绕产品的功能特性来组织工作。

  ── [map]
  EN | This is rarely successful, even in a single instance. In a portfolio of documentation instances, the results are wild inconsistency. Much better is the adoption of a scheme that tries to provide an answer to the question: how to arrange documentation *in general?*
  旧 | 即使对单个实例，这种做法也很少成功；在一组文档实例中，结果会是严重的不一致。更好的方式是采用一种方案，尝试回答：如何 *总体上* 安排文档？
  新 | 这种做法即使只在一处使用，也很少成功；放到一批文档实例里，结果便是杂乱无章的不一致。好得多的办法，是采用一套方案，试着回答这个问题：究竟该如何*总体上*安排文档？

  ── [map]
  EN | In fact any orderly attempt to organise documentation into clear content categories will help improve it (for authors as well as users), by providing lists of content types.
  旧 | 事实上，任何将文档有序组织为清晰内容类别的尝试都会有所帮助（对作者和用户皆然），因为它提供内容类型清单。
  新 | 事实上，只要把文档有条理地分进清晰的内容类别，就总能让文档有所改善（对作者如此，对用户也一样），因为它给出了内容类型的清单。

  ── [map]
  EN | Even so, authors often find themselves needing to write particular documentation content that fails to fit well within the categories put forward by a scheme, or struggling to rewrite existing material. Often, there is a sense of arbitrariness about the structure that they find themselves working with - why this particular list of content types rather than another? And if another competing list is proposed, which to adopt?
  旧 | 即便如此，作者常需撰写难以融入方案所提出类别的特定内容，或费力改写既有材料。他们使用的结构常带有任意性：为何是这份内容类型清单而非另一份？若提出了相互竞争的清单，又该采用哪一份？
  新 | 即便如此，作者也常常发现自己要写的内容偏偏塞不进方案给出的那些类别，或者为改写既有材料而大伤脑筋。对自己正在使用的那套结构，他们常有一种随意之感——为什么偏偏是这份内容类型清单，而不是另一份？假如有人提出另一份与之竞争的清单，该采用哪一份？

  ── [map]
  EN | A clear advantage of organising material this way is that it provides both clear *expectations* (to the reader) and *guidance* (to the author). It's clear what the purpose of any particular piece of content is, it specifies how it should be written and it shows where it should be placed.
  旧 | 这样组织材料的明显优势是：它同时给出清晰的 *预期* （面向读者）和 *指引* （面向作者）。每一项内容的目的很清楚，它规定应如何撰写，也显示应放在何处。
  新 | 这样组织材料，有一个明显的好处：它既给读者以清晰的*预期*，也给作者以*指引*。每一项内容的目的都一清二楚，它规定该怎么写，也指明该放在哪里。

  ── [map]
  EN | "Can you teach me to...?"
  旧 | “你能教我如何……吗？”
  新 | “你能教我怎么……吗？”

  ── [map]
  EN | "How do I...?"
  旧 | “我如何……？”
  新 | “我该怎么做……？”

  ── [map]
  EN | to describe the machinery
  旧 | 描述设备
  新 | 描述系统

  ── [map]
  EN | dry description
  旧 | 简洁严谨的描述
  新 | 平实的描述

  ── [map]
  EN | discursive explanation
  旧 | 论述式解释
  新 | 娓娓道来的解释

  ── [map]
  EN | teaching a child how to cook
  旧 | 教孩子如何烹饪
  新 | 教孩子做菜

  ── [map]
  EN | a recipe in a cookery book
  旧 | 烹饪书中的食谱
  新 | 烹饪书里的食谱

  ── [map]
  EN | an article on culinary social history
  旧 | 一篇烹饪社会史文章
  新 | 一篇关于烹饪社会史的文章

  ── [map]
  EN | Each piece of content is of a kind that not only has one particular job to do, that job is also clearly distinguished from and contrasted with the other functions of documentation.
  旧 | 每项内容不仅属于一种有特定任务的类型，其任务也与文档的其他功能清楚地区分和对照。
  新 | 每一份内容都属于某一类型：这一类型不仅有自己的一项特定任务要完成，这项任务还与文档的其他功能清楚地区别开来、形成对照。

  ── [map]
  EN | However, there is a kind of natural affinity between each of the different forms of documentation and its neighbours on the map, and a natural tendency to blur the distinctions (that can be seen repeatedly in examples of documentation).
  旧 | 然而，不同文档形式与地图上的相邻形式之间有某种天然亲和性，也自然倾向于模糊区别（在文档实例中可反复看到）。
  新 | 然而，每一种文档形式与地图上的近邻之间，都存在某种天然的亲近，也都有一种模糊彼此区别的天然倾向（这在文档实例中一再可见）。

  ── [map]
  EN | guide action
  旧 | 指导行动（行）
  新 | 引导行动（行）

  ── [map]
  EN | serve the application of skill
  旧 | 服务于技能应用（用）
  新 | 服务于技能的应用（用）

  ── [map]
  EN | serve the acquisition of skill
  旧 | 服务于技能习得（学）
  新 | 服务于技能的习得（学）

  ── [map]
  EN | When these distinctions are allowed to blur, the different kinds of documentation bleed into each other. Writing style and content make their way into inappropriate places. It also causes structural problems, which make it even more difficult to maintain the discipline of appropriate writing.
  旧 | 允许这些区别模糊时，不同类型的文档会彼此渗透。写作风格和内容会进入不适当的位置，也会造成结构问题，使维持恰当写作的纪律更加困难。
  新 | 一旦任由这些区别模糊下去，不同类型的文档就会彼此渗透。写作风格和内容会溜进本不该出现的地方。这还会造成结构问题，让人更难保持恰当写作的严谨。

  ── [map]
  EN | In the worst case there is a complete or partial collapse of tutorials and how-to guides into each other, making it impossible to meet the needs served by either.
  旧 | 最坏情况下，教程和实践指南会完全或部分坍塌为彼此，致使二者所服务的需求均无法满足。
  新 | 最坏的情况下，教程和实践指南会完全或部分地坍塌到一起，以致二者各自所服务的需求都无从满足。

  ── [map]
  EN | The journey around the map
  旧 | 围绕地图的旅程
  新 | 地图上的旅程

  ── [map]
  EN | Diátaxis is intended to help documentation better serve users in their *cycle of interaction* with a product.
  旧 | Diátaxis 旨在帮助文档在用户与产品的 *交互循环* 中更好地服务用户。
  新 | Diátaxis 旨在帮助文档在用户与产品的*交互循环*中更好地服务用户。

  ── [map]
  EN | This phrase should not be understood too literally. It is not the case that a user must encounter the different kinds of documentation in the order *tutorials* > *how-to guides* > *technical reference* > *explanation*. In practice, an actual user may enter the documentation anywhere in search of guidance on some particular subject, and what they want to read will change from moment to moment as they use your documentation.
  旧 | 不应过于字面地理解这句话。并非用户必须按 *教程* > *实践指南* > *技术参考资料* > *解释说明* 的顺序接触各类文档。实践中，用户可从任何位置进入文档，寻找特定主题的指引；随着使用文档，想读的内容会时刻变化。
  新 | 这句话不该理解得太死。并不是说，用户必须按*教程* > *实践指南* > *技术参考资料* > *解释说明*的顺序去接触各类文档。实际上，真实的用户可能从任何地方进入文档，去寻找某个具体主题的指引；而在使用你的文档的过程中，他们想读的内容时时刻刻都在变。

  ── [map]
  EN | However, the idea of a cycle of documentation needs, that proceeds through different phases, is sound and corresponds to the way that people actually do become expert in a craft. There is a sense and meaning to this ordering.
  旧 | 不过，文档需求会经历不同阶段的循环这一理念是合理的，也与人们真正成为技艺专家的方式相符。这个顺序有其意义。
  新 | 不过，文档需求构成一个循环、依次经过不同阶段，这一想法是站得住的，也与人们真正精通一门技艺的方式相符。这个顺序自有道理，也自有意义。

  ── [map]
  EN | Moving around the map
  旧 | 在地图中移动
  新 | 在地图上移动

  ── [map]
  EN | *learning-oriented phase*: We begin by learning, and learning a skill means diving straight in to do it - under the guidance of a teacher, if we're lucky.
  旧 | *面向学习的阶段*：我们从学习开始；学习一项技能意味着直接投入去做——幸运的话，有教师引导。
  新 | *面向学习的阶段*：我们从学习开始；学一项技能，就是一头扎进去动手做——运气好的话，还有教师在旁指点。

  ── [map]
  EN | *goal-oriented phase*: Next we want to put the skill to work.
  旧 | *面向目标的阶段*：接着我们希望将技能用于工作。
  新 | *面向目标的阶段*：接着，我们想把这门技能用起来。

  ── [map]
  EN | *information-oriented phase*: As soon as our work calls upon knowledge that we don't already have in our head, it requires us to consult technical reference.
  旧 | *面向信息的阶段*：工作一旦需要脑中没有的知识，就必须查阅技术参考资料。
  新 | *面向信息的阶段*：工作一旦要用到脑子里还没有的知识，我们就得去查阅技术参考资料。

  ── [map]
  EN | *explanation-oriented phase*: Finally, away from the work, we reflect on our practice and knowledge to understand the whole.
  旧 | *面向解释的阶段*：最后，离开工作后，我们反思实践与知识以理解整体。
  新 | *面向解释的阶段*：最后，我们从工作中抽身出来，反思自己的实践与知识，以理解整体。

  ── [map]
  EN | And then it's back to the beginning, perhaps for a new thing to grasp, or to penetrate deeper.
  旧 | 然后又回到起点，也许是为了掌握新事物，或是为了更深入地领会。
  新 | 然后又回到起点，也许是为了掌握一样新东西，也许是为了钻得更深。
news                       9 条  改动   3

  ── [news]
  EN | Added an atom feed, https://diataxis.fr/atom.xml.
  旧 | 已添加 Atom 订阅源：https://diataxis.fr/atom.xml。
  新 | 新增了 Atom 订阅源，https://diataxis.fr/atom.xml。

  ── [news]
  EN | `Diátaxis is now available in Polish <https://diataxis.fr/pl>`_, courtesy of the translation efforts of `Piotr Nawrot <https://piotrnawrot.com/>`_.
  旧 | `Diátaxis 现已提供波兰语版本 <https://diataxis.fr/pl>`_，这得益于 `Piotr Nawrot <https://piotrnawrot.com/>`_ 的翻译贡献。
  新 | `Diátaxis 现在有波兰语版了 <https://diataxis.fr/pl>`_，多亏 `Piotr Nawrot <https://piotrnawrot.com/>`_ 费心翻译。

  ── [news]
  EN | Other translations are in progress.
  旧 | 其他语言的翻译正在进行中。
  新 | 其他语言的翻译正在推进。
quality                   68 条  改动  58

  ── [quality]
  EN | Diátaxis is an approach to *quality* in documentation.
  旧 | Diátaxis 是一种处理文档 *质量* 的方法。
  新 | Diátaxis 是一种着眼于文档*质量*的方法。

  ── [quality]
  EN | "Quality" is a word in danger of losing some of its meaning; it's something we all approve of, but rarely risk trying to describe in any rigorous way. We want quality in our documentation, but much less often specify what exactly we mean by that.
  旧 | “质量”这个词正面临失去部分含义的危险：我们都认可它，却很少冒险尝试以严谨方式描述它。我们希望文档有质量，却更少明确说明这具体意味着什么。
  新 | “质量”这个词，正面临丢掉部分含义的危险：我们都赞成它，却很少敢冒险用严谨的方式去描述。我们希望文档有质量，却很少说清这到底指什么。

  ── [quality]
  EN | All the same, we can generally point to examples of "high-quality documentation" when asked, and can identify lapses in quality when we see them - and more than that, we often agree when we do. This suggests that we still have a useful grasp on the notion of quality.
  旧 | 尽管如此，被问到时我们通常能指出“高质量文档”的例子，也能在看到质量缺失时识别出来——更进一步，我们常会达成共识。这表明我们仍然掌握着有用的质量概念。
  新 | 话虽如此，只要被问起，我们一般都能举出“高质量文档”的例子；看到质量上的缺失，也认得出来——而且不止于此：认出来的时候，我们还常常意见一致。这说明，我们对“质量”这个概念仍然把握得住，而且这种把握是有用的。

  ── [quality]
  EN | As we pursue quality in documentation, it helps to make that grasp surer, by paying some attention to it - here, attempting to refine our grasp by positing a distinction between **functional quality** and **deep quality**.
  旧 | 在追求文档质量时，关注这一概念有助于使把握更确切。这里试图通过提出 **功能质量** 与 **深层质量** 的区分，来精炼这种把握。
  新 | 在文档中追求质量时，对这份把握多留点心，它就会更牢靠——本文所做的，就是试着提出**功能品质**与**深层品质**之分，借此把这份把握磨得更精。

  ── [quality]
  EN | Functional quality
  旧 | 功能质量
  新 | 功能品质

  ── [quality]
  EN | We need documentation to meet standards of *accuracy*, *completeness*, *consistency*, *usefulness*, *precision* and so on. We can call these aspects of its **functional quality**. Documentation that fails to meet any one of them is failing to perform one of its key functions.
  旧 | 我们需要文档符合 *准确性*、 *完整性*、 *一致性*、 *有用性*、 *精确性* 等标准。这些方面可称为其 **功能质量**。在任何一项上未达标的文档，都未能履行其一项关键功能。
  新 | 我们需要文档达到*准确性*、*完整性*、*一致性*、*有用性*、*精确性*等标准。这些方面，可以称为文档的**功能品质**。文档只要有一项没达到，就是有一项关键功能没履行。

  ── [quality]
  EN | These properties of functional quality are all independent of each other. Documentation can be accurate without being complete. It can be complete, but inaccurate and inconsistent. It can be accurate, complete, consistent and also useless.
  旧 | 功能质量的这些属性彼此独立。文档可以准确却不完整；可以完整却不准确、不一致；可以准确、完整、一致，却仍然无用。
  新 | 功能品质的这些属性彼此独立。文档可以准确，却不完整；可以完整，却不准确、不一致；也可以准确、完整、一致，却依然无用。

  ── [quality]
  EN | Attaining functional quality means meeting high, objectively-measurable standards in multiple independent dimensions, consistently. It requires discipline and attention to detail, and high levels of technical skill.
  旧 | 实现功能质量，意味着在多个独立维度上一贯达到高且可客观衡量的标准。这要求纪律、对细节的关注和高水平的技术能力。
  新 | 要达成功能品质，就得在多个彼此独立的维度上，持续达到很高且可客观衡量的标准。这需要严谨自律、留意细节，以及高超的技术能力。

  ── [quality]
  EN | To make it harder for the creator of documentation, any failure to meet all of these standards is readily apparent to the user.
  旧 | 更令文档创建者头疼的是，任何未满足这些标准的地方，用户都很容易察觉。
  新 | 更让文档创建者头疼的是，任何一处没达到这些标准，用户都一眼就能看出来。

  ── [quality]
  EN | Deep quality
  旧 | 深层质量
  新 | 深层品质

  ── [quality]
  EN | There are other characteristics, that we can call **deep quality**.
  旧 | 还有其他一些特质，可以称为 **深层质量**。
  新 | 还有另一些特征，我们可以称之为**深层品质**。

  ── [quality]
  EN | Functional quality is not enough, or even satisfactory on its own as an ambition. True excellence in documentation implies characteristics of quality that are not included in accuracy, completeness and so on.
  旧 | 仅有功能质量并不足够；以它作为唯一的追求，甚至不能令人满意。文档真正的卓越，意味着具有不包含在准确性、完整性等之内的质量特征。
  新 | 功能品质还不够，单把它当追求目标，甚至谈不上令人满意。文档真正的卓越，意味着它还具备一些超出准确性、完整性等范畴的质量特征。

  ── [quality]
  EN | Think of characteristics such as:
  旧 | 想想如下特质：
  新 | 想想这样一些特征：

  ── [quality]
  EN | *feeling good to use*
  旧 | *使用感受良好*
  新 | *用起来感觉好*

  ── [quality]
  EN | Unlike the characteristics of functional quality, they cannot be checked or measured, but they can still be clearly identified. When we encounter them, we usually (not always, because we need to be capable of it) recognise them.
  旧 | 不同于功能质量的属性，这些特质无法检查或衡量，但仍可清楚识别。遇到它们时，我们通常（并非总是，因为需要具备这种能力）会认得出来。
  新 | 与功能品质的特征不同，它们无法查验、无法衡量，却仍能清楚地辨认出来。遇上它们时，我们通常（并非总是如此，因为要认出来，我们自己得有这份能力）认得出它们。

  ── [quality]
  EN | They are characteristics of *deep quality*.
  旧 | 它们是 *深层质量* 的特征。
  新 | 它们是*深层品质*的特征。

  ── [quality]
  EN | What's the difference?
  旧 | 区别是什么？
  新 | 区别在哪儿？

  ── [quality]
  EN | Aspects of deep quality seem to be genuinely distinct in kind from the characteristics of functional quality.
  旧 | 深层质量的方面在性质上似乎确实不同于功能质量的特征。
  新 | 深层品质的各个方面，与功能品质的特征似乎确有种类之别。

  ── [quality]
  EN | Documentation can meet all the demands of functional quality, and still fail to exhibit deep quality. There are many examples of documentation that is accurate and consistent (and even very useful) but which is also awkward and unpleasant to use.
  旧 | 文档可以满足功能质量的一切要求，却仍未表现出深层质量。有许多文档准确、一致（甚至非常有用），却使用起来笨拙而不愉快。
  新 | 文档可以满足功能品质的一切要求，却依然表现不出深层品质。这样的例子不少：有些文档准确、一致（甚至非常有用），用起来却别扭、令人不快。

  ── [quality]
  EN | It's also noticeable that while characteristics of functional quality such as completeness and accuracy are **independent** of each other, those of deep quality are hard to disentangle. *Having flow* and *anticipating the user* are aspects of each other - they are **interdependent**. It's hard to see how something could feel good to use without fitting to our needs.
  旧 | 功能质量的完整性、准确性等特征彼此 **独立**；而深层质量的特征则难以拆开。 *流畅感* 与 *预见用户所需* 彼此交织，具有 **相互依赖性**。很难想象某物不契合我们的需求，却能让人使用感受良好。
  新 | 同样值得注意的是：完整性、准确性这类功能品质的特征彼此**独立**，而深层品质的特征却纠缠难分。*具有流畅感*与*预见用户所需*互为彼此的方面——它们**相互依存**。很难想象一样东西不契合我们的需求，却用起来感觉良好。

  ── [quality]
  EN | Aspects of functional quality can be measured - literally, with numbers, in some cases (consider completeness). That's clearly not possible with qualities such as *having flow*. Instead, such qualities can only be enquired into, interrogated. Instead of taking **measurements**, we must make **judgements**.
  旧 | 功能质量的方面可以衡量——有时确实可用数字衡量（如完整性）。对于 *流畅感* 这类质量显然做不到。此类质量只能被探究、审视；我们不能进行 **测量**，而必须作出 **判断**。
  新 | 功能品质的各个方面是可以衡量的——有些甚至真的能用数字来衡量（想想完整性）。而*具有流畅感*这类品质，显然做不到。这样的品质只能去探问、去追问。我们不能做**测量**，只能下**判断**。

  ── [quality]
  EN | Functional quality is **objective** - it belongs to the world. Accuracy of documentation means the extent to which it conforms to the world it’s trying to describe. Deep quality can’t be ascertained by holding something up to the world. It’s **subjective**, which means that we can assess it only in the light of the needs of the subject of experience, the human.
  旧 | 功能质量是 **客观的** ——它属于世界。文档的准确性指其符合所描述世界的程度。深层质量无法通过把事物与世界比照来确定；它是 **主观的**，意味着只能依体验主体即人的需求来评估。
  新 | 功能品质是**客观的**——它属于世界。文档的准确性，指的是它在多大程度上符合它试图描述的那个世界。深层品质却无法靠把某样东西拿到世界面前比照来确认。它是**主观的**，也就是说，我们只能依据体验主体即人的需求来评判它。

  ── [quality]
  EN | And, deep quality is **conditional** upon functional quality. Documentation can be accurate and complete and consistent without being truly excellent - but it will never have deep quality without being accurate and complete and consistent. No user of documentation will experience it as beautiful, if it's inaccurate, or enjoy the way it anticipates their needs if it's inconsistent. The moment we run into such lapses the experience of documentation is tarnished.
  旧 | 深层质量又以功能质量为 **条件**。文档可以准确、完整且一致却并不真正卓越；但若不准确、完整和一致，就绝不会有深层质量。文档不准确，用户不会觉得它优美；文档不一致，用户也不会享受它对需求的预见。遇到这类缺失时，文档体验便会蒙尘。
  新 | 而且，深层品质以功能品质为**条件**。文档可以准确、完整、一致，却并不真正卓越——但只要做不到准确、完整、一致，它就永远不会有深层品质。文档不准确，没有哪个用户会觉得它美；不一致，也没有谁会喜欢它预判需求的样子。一旦撞上这类缺失，文档体验就此失去光泽。

  ── [quality]
  EN | Finally, all of the characteristics of functional quality appear to us, as documentation creators, as burdens and **constraints**. Each one of them represents a test or challenge we might fail. Or, even if we have met one *now*, we can never rest, because the next release or update means that we'll have to check our work once again, against the thing that it's documenting. Characteristics such as anticipating needs or flow, on the other hand, represent **liberation**, the work of creativity or taste. To attain functional quality in our work, we must *conform* to constraints; to attain deep quality we must *invent*.
  旧 | 最后，对文档创建者而言，功能质量的一切特征都像负担和 **约束**：每一项都是可能失败的检验或挑战。即使现在已满足其中一项，也不能松懈，因为下一次发布或更新意味着必须再次将工作与所记录的对象核对。反之，预见需求或流畅感代表的是 **解放**，即创造力或品味的工作。要实现功能质量，必须 *遵从* 约束；要实现深层质量，必须 *创造*。
  新 | 最后，在我们这些文档创建者眼里，功能品质的一切特征都是负担与**约束**：每一项都是一道我们可能通不过的检验或挑战。又或者，即使*此刻*已经满足了一项，也永远不能歇息——因为下一次发布或更新，就意味着我们还得对照它所描述的那个东西，把工作再核对一遍。而预见需求、流畅感这类特征，代表的则是**解放**，是创造力与品味的工作。要在工作中达成功能品质，我们必须*遵从*约束；要达成深层品质，我们必须*创造*。

  ── [quality]
  EN | independent characteristics
  旧 | 独立特征
  新 | 彼此独立的特征

  ── [quality]
  EN | interdependent characteristics
  旧 | 相互依赖的特征
  新 | 彼此依存的特征

  ── [quality]
  EN | measured against the world
  旧 | 与世界比照衡量
  新 | 以世界为尺度衡量

  ── [quality]
  EN | assessed against the human
  旧 | 依人来评估
  新 | 以人为尺度评估

  ── [quality]
  EN | a condition of deep quality
  旧 | 深层质量的条件
  新 | 深层品质的条件

  ── [quality]
  EN | conditional upon functional quality
  旧 | 以功能质量为条件
  新 | 以功能品质为条件

  ── [quality]
  EN | aspects of constraint
  旧 | 约束的方面
  新 | 约束的一面

  ── [quality]
  EN | aspects of liberation
  旧 | 解放的方面
  新 | 解放的一面

  ── [quality]
  EN | How we recognise deep quality
  旧 | 我们如何识别深层质量
  新 | 我们如何认出深层品质

  ── [quality]
  EN | Consider how we judge the quality of say, clothing. Clothes must have *functional quality* (they must keep us appropriately warm and dry, stand up to wear). These things are objectively measurable. You don't really need to know much about clothes to assess how well they do those things. If water gets in, or the clothing falls apart - it lacks quality.
  旧 | 想想我们如何判断衣物质量。衣物必须具有 *功能质量* （恰当保暖、保持干燥、经得起穿着），这些可客观衡量。无需很懂衣服，也能评估它们做得如何：若进水或衣服散架，就缺乏质量。
  新 | 就拿衣服来说吧，想想我们怎么判断它的质量。衣服必须具备*功能品质*（必须让我们该暖时暖、该干时干，还经得起穿）。这些都是可以客观衡量的。衣服在这些事上做得怎么样，不需要你多懂衣服就能判断出来。水一旦渗进来，或者衣服散了架——那就是缺了质量。

  ── [quality]
  EN | There are other characteristics of quality in clothing that can't simply be measured objectively, and to recognise those characteristics, we need to have an understanding of clothing. The quality of materials or workmanship isn't always immediately obvious. Being able to judge that an item of clothing hangs well, moves well or has been expertly shaped requires developing at least a basic eye for those things. And these are its characteristics of *deep quality*.
  旧 | 衣物还有其他无法简单客观衡量的质量特征；要识别它们，需理解衣物。材料或工艺的质量并非总是立即显见。要判断衣物是否垂坠得体、活动自如或剪裁精湛，需要培养至少基本的眼光。这些便是它的 *深层质量* 特征。
  新 | 衣服还有些质量特征，无法简单地客观衡量；要认出这些特征，我们得懂一点衣服。面料或做工的好坏，并不总是一眼就能看出来。要判断一件衣服是否垂得好、动得顺，剪裁是否出自行家之手，至少得对这类事情培养出一点基本的眼力。这些，就是它的*深层品质*特征。

  ── [quality]
  EN | But: even someone who can't recognise, or fails to understand, those characteristics - who cannot say *what* they are - can still recognise very well *that* the clothing is excellent, because they find it that **it feels good to wear**, because it's such that they want to wear it. No expertise is required to realise that clothing does or doesn't feel comfortable as you move in it, that it fits and moves with you well. *Your body knows it*.
  旧 | 不过，即使无法识别或理解这些特征、说不出 *是什么*，仍能很好地认出衣物是卓越的，因为觉得它 **穿着舒适**，想穿它。无需专业知识也能知道衣服活动时是否舒适、是否合身且随身体自然移动。 *你的身体知道。*
  新 | 但是：即使有人认不出、也理解不了这些特征——说不出它们*是什么*——仍然能清清楚楚地认出这件衣服*确实*卓越，因为他发觉它**穿着舒服**，因为它让他想穿。衣服在你活动时舒不舒服、是否贴合并随你而动，这不需要任何专业本领就能察觉。*你的身体知道*。

  ── [quality]
  EN | And it's the same in documentation. Perhaps you need to be a connoisseur to recognise *what* it is that makes some documentation excellent, but that's not necessary to be able to realise *that* it is excellent. Good documentation **feels good**; you feel pleasure and satisfaction when you use it - it feels like it fits and moves with you.
  旧 | 文档也是如此。也许需要行家才能认识到某些文档卓越的 *原因*，但无需如此才能知道它 *确实* 卓越。好文档 **感觉良好**；使用时会感到愉悦和满足，像是它契合你并随你一起移动。
  新 | 文档也是一样。要看出某些文档*好在哪里*，也许你得是行家；但要意识到它*确实*好，却不必如此。好的文档**手感是好的**；用起来你会感到愉悦、满足——感觉它贴合你，随你而动。

  ── [quality]
  EN | The users of our documentation may or may not have the understanding to say why it's good, or where its quality lapses. They might recognise only the more obvious aspects of functional quality in it, mistaking those for its deeper excellence. That doesn't matter - it will feel good, or not, and that's what is important.
  旧 | 文档用户可能理解也可能不理解它为何好、质量在哪些地方缺失。他们或许只能识别功能质量中较显而易见的方面，并误认为那就是更深的卓越。这并不重要——它会让人感觉良好，或者不会，这才重要。
  新 | 我们文档的用户，未必说得清它为什么好、质量又在哪里失了水准。他们可能只认得出其中比较显眼的功能品质，还误以为那就是更深的卓越。这没关系——它会让人感觉好，或者不好，而这才是要紧的。

  ── [quality]
  EN | But we, as its creators, need a clear and effective understanding of what makes documentation good. We need to develop our sense of it so that we recognise *what* is good about it, as well as *that* it is good. And we need to develop an understanding of how people will *feel* when they're using it.
  旧 | 但作为创建者，我们需要清楚而有效地理解文档为何优秀。必须培养这种感受，以便既认识到它 *确实* 好，也认识到它 *好在哪里*；还须理解人们使用它时会有何种 *感受*。
  新 | 但我们身为它的创建者，需要清楚而有效地理解是什么让文档变好。我们需要培养自己对它的感觉，既看出它*好在哪里*，也看出它*确实*好。我们还需要理解，人们使用它时会有怎样的*感受*。

  ── [quality]
  EN | Producing work of deep quality depends on our ability to do this.
  旧 | 能否产出具有深层质量的作品，取决于我们做到这一点的能力。
  新 | 能否做出有深层品质的作品，就看我们有没有这份本事。

  ── [quality]
  EN | Functional quality's obligations are met through conscientious observance of the demands of the craft of documentation. They require solid skill and knowledge of the technical domain, the ability to gather up a complete terrain into a single, coherent, consistent map of it.
  旧 | 功能质量的责任通过认真遵守文档技艺的要求来履行。它们需要扎实的技能和技术领域知识，以及将完整领域汇集成单一、连贯、一致地图的能力。
  新 | 功能品质的义务，靠认真遵守文档技艺的要求来履行。这要求扎实的技能、技术领域的知识，以及把完整的一片地形收拢成一幅单一、连贯、一致的地图的能力。

  ── [quality]
  EN | **Diátaxis cannot address functional quality in documentation.** It is concerned only with certain aspects of deep quality, some more than others - though if all the aspects of deep quality are tangled up in each other, then it affects all of them.
  旧 | **Diátaxis 无法解决文档的功能质量。** 它只关注深层质量的某些方面——有的方面多一些，有的少一些；不过，如果深层质量的所有方面都彼此缠绕，那么它也会影响到所有方面。
  新 | **Diátaxis 无法解决文档的功能品质。**它只关心深层品质的某些方面——对有些方面关心得多些，有些少些。不过，如果深层品质的所有方面都彼此缠绕，那它也就影响到了所有方面。

  ── [quality]
  EN | Exposing lapses in functional quality
  旧 | 暴露功能质量缺失
  新 | 暴露功能品质的缺失

  ── [quality]
  EN | Although Diátaxis cannot address, or *give* us, functional quality, it can still serve it.
  旧 | 尽管 Diátaxis 无法处理或 *给予* 我们功能质量，它仍能服务于功能质量。
  新 | 尽管 Diátaxis 无法解决、也无法*给予*我们功能品质，它仍然能为之效力。

  ── [quality]
  EN | It works very effectively to *expose* lapses in functional quality. It's often remarked that one effect of applying Diátaxis to existing documentation is that problems in it suddenly become apparent that were obscured before.
  旧 | 它非常有效地 *暴露* 功能质量的缺失。人们常说，将 Diátaxis 应用于既有文档的一个效果，是先前被遮蔽的问题会突然变得明显。
  新 | 它非常有效地*暴露*出功能品质的缺失。人们常说，把 Diátaxis 用于既有文档，一个效果就是：原先被遮蔽的问题会突然显现出来。

  ── [quality]
  EN | For example: the Diátaxis approach recommends that :ref:`the architecture of reference documentation should reflect the architecture of the code it documents <respect-structure>`. This makes gaps in the documentation much more clearly visible.
  旧 | 例如，Diátaxis 方法建议 :ref:`参考资料的架构应反映其所记录代码的架构 <respect-structure>`。这让文档中的缺口清晰得多。
  新 | 例如，Diátaxis 方法主张：:ref:`参考资料的架构应当反映它所描述的代码的架构 <respect-structure>`。这样一来，文档中的缺口就清楚得多了。

  ── [quality]
  EN | Or, moving explanatory verbiage out of a tutorial (in accordance with Diátaxis demands) often has the effect of highlighting a section where the reader has been left to work something out for themselves.
  旧 | 又如，按 Diátaxis 的要求将解释性冗文从教程移出，往往会凸显一个章节：读者原先被留在那里，只能自行弄清某件事。
  新 | 又比如，按 Diátaxis 的要求把解释性的冗词从教程里挪走，往往会让某一节凸显出来——那一节里，读者被撇在一边，只能自己琢磨出个究竟。

  ── [quality]
  EN | But, as far as functional quality goes, Diátaxis principles can have only an *analytical* role.
  旧 | 不过就功能质量而言，Diátaxis 原则只能发挥 *分析性* 作用。
  新 | 但就功能品质而言，Diátaxis 的原则只能发挥*分析性*的作用。

  ── [quality]
  EN | Creating deep quality
  旧 | 创造深层质量
  新 | 创造深层品质

  ── [quality]
  EN | In deep quality on the other hand, the Diátaxis approach can do more.
  旧 | 而在深层质量方面，Diátaxis 方法可以做得更多。
  新 | 而在深层品质这一边，Diátaxis 方法能做的就更多了。

  ── [quality]
  EN | For example, it helps documentation *fit user needs* by describing documentation modes that are based on them; its categories exist as a response to needs.
  旧 | 例如，它通过描述基于用户需求的文档模式，帮助文档 *契合用户需求*；它的类别正是为回应需求而存在。
  新 | 例如，它描述出以用户需求为根据的文档模式，从而帮助文档*契合用户需求*；它的那些类别，正是为回应需求而存在。

  ── [quality]
  EN | We must pay attention to the correct organisation of these categories then, and the arrangement of its material and the relationships within them, the form and language adopted in different parts of documentation - as a way of fitting to user needs.
  旧 | 因此，必须关注这些类别的正确组织、材料的编排及其中的关系，以及文档不同部分采用的形式与语言——这些都是契合用户需求的方式。
  新 | 因此，我们必须留意：这些类别是否组织得当，材料如何编排、其间关系如何，以及文档不同部分采用的形式与语言——这一切都是为了契合用户需求。

  ── [quality]
  EN | Or, in Diátaxis we are directly concerned with *flow*. In flow - whether the context is documentation or anything else - we experience a movement from one stage or state to another that seems right, unforced and in sympathy with both our concerns of the moment, and the way our minds and bodies work in general.
  旧 | 又如，在 Diátaxis 中，我们直接关心 *流畅感*。在流畅中——无论语境是文档还是其他事物——我们体验到从一个阶段或状态到另一阶段或状态的移动；它恰当、不勉强，且与当下关切以及心智和身体的一般运作方式相协调。
  新 | 又比如，在 Diátaxis 里，我们直接关心的是*流畅感*。身处流畅之中——无论语境是文档还是别的什么——我们会感到自己从一个阶段或状态移动到了另一个阶段或状态，而这种移动显得恰当、不勉强，既与我们此刻的关切合拍，也与我们的心智和身体通常的运作方式合拍。

  ── [quality]
  EN | Diátaxis preserves flow by helping prevent the kind of disruption of rhythm that occurs when something runs across our purpose and steady progress towards it (for example when a digression into explanation interrupts a how-to guide).
  旧 | Diátaxis 通过帮助避免那种节奏中断来保持流畅感：当某物横亘在目标和朝向目标的稳定进展之间时，便会产生这种中断（例如解释说明的旁枝打断实践指南）。
  新 | Diátaxis 保住流畅感，靠的是帮着防止一种节奏断裂——当我们正朝目的稳步前进时，若有东西横插进来，节奏就断了（例如一段解释的闲笔打断了实践指南）。

  ── [quality]
  EN | It's important to understand that Diátaxis can never be *all* that is required in the pursuit of deep quality.
  旧 | 必须理解，在追求深层质量时，Diátaxis 永远不可能是所需的一切。
  新 | 有一点必须明白：在追求深层品质时，Diátaxis 永远不可能是所需的*全部*。

  ── [quality]
  EN | For example, while it can *help* attain beauty in documentation, at least in its overall form, it doesn't by itself *make documentation beautiful*.
  旧 | 例如，它可以 *帮助* 文档实现优美，至少在整体形式上如此，但它本身并不会 *让文档变得优美*。
  新 | 例如，它至少能在整体形式上*帮助*文档达到优美，但它本身并不能*让文档变得优美*。

  ── [quality]
  EN | Diátaxis offers a set of principles - it doesn't offer a formula. It certainly cannot offer a short-cut to success, bypassing the skills and insights of disciplines such as user experience or user interaction design, or even visual design.
  旧 | Diátaxis 提供一组原则，而非公式。它当然不能提供通往成功的捷径，绕过用户体验、用户交互设计，甚至视觉设计等领域的技能和洞见。
  新 | Diátaxis 给出的是一套原则，不是一条公式。它当然也给不出通往成功的捷径，去绕过用户体验、用户交互设计乃至视觉设计这些专业领域里的技能与洞见。

  ── [quality]
  EN | Using Diátaxis does not guarantee deep quality. The characteristics of deep quality are forever being renegotiated, reinterpreted, rediscovered and reinvented. But what Diátaxis *can* do is lay down some conditions for the *possibility* of deep quality in documentation.
  旧 | 使用 Diátaxis 并不保证深层质量。深层质量的特征会不断被重新协商、重新诠释、重新发现和重新创造；但 Diátaxis *能够* 做的是，为文档中深层质量的 *可能性* 奠定一些条件。
  新 | 用 Diátaxis，并不保证就有深层品质。深层品质的特征，永远在被重新协商、重新诠释、重新发现、重新创造。但 Diátaxis *能够*做的，是为文档中深层品质的*可能性*设下若干条件。
reference                 45 条  改动  36

  ── [reference]
  EN | Reference guides are **technical descriptions** of the machinery and how to operate it. Reference material is **information-oriented**.
  旧 | 参考指南是对设备及其操作方式的 **技术描述**。参考资料是 **面向信息** 的。
  新 | 参考指南是对系统本身及其操作方式的**技术描述**。参考资料是**面向信息**的。

  ── [reference]
  EN | Reference material contains *propositional or theoretical* knowledge that a user looks to in their *work*.
  旧 | 参考资料包含用户在 *工作* 中查阅的 *命题性或理论性* 知识。
  新 | 参考资料包含*命题性或理论性*知识，供用户在*工作*中查阅。

  ── [reference]
  EN | The only purpose of a reference guide is to describe, as succinctly as possible, and in an orderly way. Whereas the content of tutorials and how-to guides are led by needs of the user, reference material is led by the product it describes.
  旧 | 参考指南唯一的目的是以尽可能简洁、有序的方式进行描述。教程和实践指南的内容由用户需求引领；参考资料则由其描述的产品引领。
  新 | 参考指南唯一的用途就是描述——尽可能简洁，而且有条不紊。教程和实践指南的内容由用户需求引领；参考资料则由它所描述的产品引领。

  ── [reference]
  EN | Reference - information oriented, theoretical knowledge, that serves our work
  旧 | 参考资料——面向信息，以理论性知识（知）服务于技能应用（用）
  新 | 参考资料——面向信息，以理论性知识（知）服务于技能的应用（用）

  ── [reference]
  EN | In the case of software, reference guides describe the software itself - APIs, classes, functions and so on - and how to use them.
  旧 | 在软件场景中，参考指南描述软件本身——API、类、函数等——以及它们的使用方式。
  新 | 就软件而言，参考指南描述软件本身——API、类、函数等——以及如何使用它们。

  ── [reference]
  EN | Your users need reference material because they need truth and certainty - firm platforms on which to stand while they work. Good technical reference is essential to provide users with the confidence to do their work.
  旧 | 用户需要参考资料，因为他们需要真相和确定性——在工作时可以立足的坚实平台。良好的技术参考资料，对于用户建立起完成工作的信心至关重要。
  新 | 你的用户需要参考资料，因为他们需要真相与确定性——一块让他们在工作时站得稳的坚实平台。优秀的技术参考资料不可或缺，它让用户有底气去做自己的工作。

  ── [reference]
  EN | Reference as description
  旧 | 作为描述的参考资料
  新 | 参考资料即描述

  ── [reference]
  EN | Reference material describes the machinery. It should be **austere**. One hardly *reads* reference material; one *consults* it.
  旧 | 参考资料描述设备，应当 **严谨克制**。人们几乎不 *阅读* 参考资料，而是 *查阅* 它。
  新 | 参考资料描述的是系统本身，应当**严谨克制**。人们几乎不*阅读*参考资料，而是*查阅*它。

  ── [reference]
  EN | There should be no doubt or ambiguity in reference; it should be wholly authoritative.
  旧 | 参考资料中不应有疑义或含混；它应当完全权威。
  新 | 参考资料不容半点疑惑或含混；它必须完全权威。

  ── [reference]
  EN | Reference material is like a map. A map tells you what you need to know about the territory, without having to go out and check the territory for yourself; a reference guide serves the same purpose for the product and its internal machinery.
  旧 | 参考资料像一张地图。地图无需你亲自去勘察地形，便告诉你需要了解的领域信息；参考指南对产品及其内部机制的作用相同。
  新 | 参考资料就像一张地图。地图会告诉你关于一片地域你需要知道的一切，用不着你亲自出去查看；参考指南对产品及其内部构造，也起着同样的作用。

  ── [reference]
  EN | Although reference should not attempt to show how to perform tasks, it can and often needs to include a description of how something works or the correct way to use it.
  旧 | 虽然参考资料不应试图展示如何完成任务，却可以且常常需要说明某物的运作方式或正确使用方式。
  新 | 虽然参考资料不应试图展示如何完成任务，却可以，而且往往需要描述某物如何运作，或者它的正确用法。

  ── [reference]
  EN | Unfortunately, too many software developers think that auto-generated reference material is all the documentation required.
  旧 | 遗憾的是，太多软件开发者认为自动生成的参考资料就是所需的全部文档。
  新 | 遗憾的是，太多软件开发者以为，自动生成的参考资料就是所需的全部文档。

  ── [reference]
  EN | Some reference material (such as API documentation) can be generated automatically by the software it describes, which is a powerful way of ensuring that it remains faithfully accurate to the code.
  旧 | 一些参考资料（如 API 文档）可由其描述的软件自动生成，这是确保其始终忠实准确地反映代码的一种有力方式。
  新 | 有些参考资料（如 API 文档）可以由它所描述的软件自动生成，这是确保它始终忠实于代码、准确无误的有力手段。

  ── [reference]
  EN | Describe and only describe
  旧 | 只作描述
  新 | 描述，只有描述

  ── [reference]
  EN | *Neutral description* is the key imperative of technical reference.
  旧 | *中立的描述* 是技术参考资料的关键要求。
  新 | *中立的描述*是技术参考资料的第一要义。

  ── [reference]
  EN | austere and uncompromising
  旧 | 严谨克制，毫不妥协
  新 | 严谨克制、毫不妥协

  ── [reference]
  EN | structured according to the structure of the machinery itself
  旧 | 按设备本身的结构组织
  新 | 按系统本身的结构来组织

  ── [reference]
  EN | Unfortunately one of the hardest things to do is to describe something neutrally. It's not a natural way of communicating. What's natural on the other hand is to explain, instruct, discuss, opine, and all these things run counter to the needs of technical reference, which instead demands accuracy, precision, completeness and clarity.
  旧 | 遗憾的是，中立地描述某物是最难做到的事情之一。这并非自然的沟通方式；相反，解释、指导、讨论、发表观点才更自然，而这些都违背技术参考资料的需求——它要求准确、精确、完整和清晰。
  新 | 遗憾的是，最难做到的事情之一，就是中立地描述一样东西。这并非自然的沟通方式。相比之下，解释、指导、讨论、发表意见才是自然的，而这一切都与技术参考资料的需求背道而驰，它要的却是准确、精确、完整、清晰。

  ── [reference]
  EN | It can be tempting to introduce instruction and explanation, simply because description can seem too inadequate to be useful, and because we do indeed need these other things. Instead, link to how-to guides, explanation and introductory tutorials.
  旧 | 很容易引入指导和解释，因为描述可能显得不足以发挥作用，也因为我们确实需要这些内容。应转而链接到实践指南、解释说明和入门教程。
  新 | 人难免想引入指导和解释，只因为描述似乎太单薄、派不上用场，也因为我们确实需要这些别的东西。那就改为链接到实践指南、解释说明和入门教程。

  ── [reference]
  EN | **Reference material is useful when it is consistent.** Standard patterns are what allow us to use reference material effectively. Your job is to place the material that your user needs where they expect to find it, in a format that they are familiar with.
  旧 | **参考资料保持一致时才有用。** 标准模式让我们能有效使用参考资料。你的工作是将用户所需的材料放在其期望找到的位置，并以他们熟悉的格式呈现。
  新 | **参考资料只有保持一致才有用。**有了标准模式，我们才能有效地使用参考资料。你的任务，就是把你的用户所需的材料，放在他们预期能找到的地方，用他们熟悉的格式呈现。

  ── [reference]
  EN | There are many opportunities in writing to delight your readers with your extensive vocabulary and command of multiple styles, but reference material is definitely not one of them.
  旧 | 写作中有许多机会可用丰富词汇和多样风格取悦读者，但参考资料绝不是其中之一。
  新 | 写作中有的是机会，让你凭广博的词汇量和驾驭多种文风的本事博得读者欢心，但参考资料绝对不在此列。

  ── [reference]
  EN | Respect the structure of the machinery
  旧 | 尊重设备的结构
  新 | 尊重系统自身的结构

  ── [reference]
  EN | The way a map corresponds to the territory it represents helps us use the former to find our way through the latter. It should be the same with documentation: **the structure of the documentation should mirror the structure of the product**, so that the user can work their way through them at the same time.
  旧 | 地图与其所表示地形的对应方式，帮助我们借助前者穿行后者。文档也应如此： **文档的结构应映照产品的结构**，使用户能够同时在二者中找到路径。
  新 | 地图与它所表示的地域相互对应，正是这种对应，让我们能借助地图在这片地域中找到路。文档也该如此：**文档的结构应当映照产品的结构**，好让用户能同时在两者中一路走下去。

  ── [reference]
  EN | It doesn't mean forcing the documentation into an unnatural structure. What's important is that the logical, conceptual arrangement of and relations within the code should help make sense of the documentation.
  旧 | 这不意味着要把文档强塞进不自然的结构。重要的是，代码的逻辑和概念编排及其中的关系，应有助于理解文档。
  新 | 这不意味着要把文档硬塞进一个不自然的结构里。重要的是，代码在逻辑与概念上的编排，还有代码内部的关系，都应当有助于理解文档。

  ── [reference]
  EN | **Examples** are valuable ways of providing illustration that helps readers understand reference, while avoiding the risk of becoming distracted from the job of describing. For example, an example of usage of a command can be a succinct way of illustrating it and its context, without falling into the trap of trying to explain or instruct.
  旧 | **示例** 是很有价值的说明方式，既帮助读者理解参考资料，又避免偏离描述本职。例如，一条命令的使用示例可以简洁说明它及其语境，而不会落入试图解释或指导的陷阱。
  新 | **示例**是很有价值的说明手段，既帮助读者理解参考资料，又避免了偏离描述本职的风险。比如，给出某条命令的用法示例，就能简洁地说明它及其语境，而不至于落入试图解释或指导的陷阱。

  ── [reference]
  EN | Django's default logging configuration inherits Python's defaults. It's available as ``django.utils.log.DEFAULT_LOGGING`` and defined in ``django/utils/log.py``
  旧 | Django 的默认日志配置继承 Python 的默认配置。它以 ``django.utils.log.DEFAULT_LOGGING`` 提供，并定义在 ``django/utils/log.py`` 中。
  新 | Django 的默认日志配置继承 Python 的默认配置。它以 ``django.utils.log.DEFAULT_LOGGING`` 的形式提供，定义在 ``django/utils/log.py`` 中。

  ── [reference]
  EN | State facts about the machinery and its behaviour.
  旧 | 陈述关于设备及其行为的事实。
  新 | 陈述关于系统及其行为的事实。

  ── [reference]
  EN | You must use a. You must not apply b unless c. Never d.
  旧 | 必须使用 a；除非满足 c，否则不得应用 b；绝不可使用 d。
  新 | 你必须使用 a。除非满足 c，否则不得应用 b。绝不要用 d。

  ── [reference]
  EN | Provide warnings where appropriate.
  旧 | 在适当处给出警告。
  新 | 在适当之处给出警告。

  ── [reference]
  EN | Applied to food and cooking
  旧 | 应用到食物和烹饪
  新 | 应用于食物与烹饪

  ── [reference]
  EN | You might check the information on a packet of food, in order to help you make a decision about what to do.
  旧 | 你可能会查看食品包装上的信息，以帮助自己决定该怎么做。
  新 | 你可能会查看食品包装上的信息，好帮自己决定该怎么做。

  ── [reference]
  EN | When you're looking for information - relevant facts - you do not want to be confronted by opinions, speculation, instructions or interpretation.
  旧 | 当查找信息——相关事实——时，你不希望面对观点、推测、指令或解释。
  新 | 你在查找信息——即相关的事实——时，并不想迎面撞上观点、推测、指令或解读。

  ── [reference]
  EN | You also expect that information to be presented in standard ways, so that you - when you need to know about something's nutritional properties, how it should be stored, its ingredients, what health implications it might have - can find them quickly, and know you can rely on them.
  旧 | 你也期望这些信息以标准方式呈现，这样，当需要了解食物的营养属性、储存方法、成分或可能的健康影响时，就能快速找到，并相信它们可靠。
  新 | 你还期望这些信息以标准方式呈现，这样——当你需要了解某样东西的营养特性、该如何储存、有哪些配料、可能有什么健康影响时——你就能迅速找到它们，并且知道它们靠得住。

  ── [reference]
  EN | So you expect to see for example: *May contain traces of wheat*. Or: *Net weight: 1000g*.
  旧 | 因此，你会期待看到例如： *可能含有小麦痕量成分*，或： *净含量：1000 克*。
  新 | 所以你会期待看到这样的字样，例如：*可能含有微量小麦*。或者：*净含量：1000 克*。

  ── [reference]
  EN | You will certainly not expect to find for example recipes or marketing claims mixed up with this information; that could be literally dangerous.
  旧 | 你当然不会希望食谱或营销宣传混杂在这些信息中；那确实可能造成危险。
  新 | 像食谱、营销话术这类东西，你绝不会期望它们跟这些信息混在一起；那真的可能造成危险。

  ── [reference]
  EN | The way reference material is presented on food products is so important that it's usually governed by law, and the same kind of seriousness should apply to all reference documentation.
  旧 | 食品包装上参考资料的呈现方式如此重要，以致通常受法律约束；同样的严肃性，也应适用于所有参考文档。
  新 | 食品包装上参考资料的呈现方式，重要到通常要由法律来管；同样的严肃态度，也应当用在所有参考资料上。
reference-explanation     22 条  改动  19

  ── [reference-explanation]
  EN | Explanation and reference both belong to the *theory* half of the Diátaxis map - they don't contain steps to guide the reader, they contain theoretical knowledge.
  旧 | 解释说明和参考资料都属于 Diátaxis 地图中 **知（认知）** 的一侧：它们不包含引导读者的步骤，而是提供理论知识。
  新 | 解释说明和参考资料同属 Diátaxis 地图的*理论*一侧——它们不包含引导读者的步骤，包含的是理论知识。

  ── [reference-explanation]
  EN | The difference between them is - just as in the difference between tutorials and how-to guides - the difference between the *acquisition* of skill and knowledge, and its *application*. In other words it's the distinction between *study* and *work*.
  旧 | 二者的区别——正如教程和实践指南的区别——在于 **学（习得）** 与 **用（应用）**：前者关注习得技能与知识，后者关注应用它们。换言之，即 *学习* 与 *工作* 的区别。
  新 | 二者的区别——正如教程和实践指南的区别——就在于技能与知识的*学（习得）*与*用（应用）*。换言之，就是*学*与*用*的区别。

  ── [reference-explanation]
  EN | A straightforward distinction, *mostly*
  旧 | 一个大体上直观的区别
  新 | 一个简单明了的区别，*大体上*

  ── [reference-explanation]
  EN | Mostly it's fairly straightforward to recognise whether you're dealing with one or the other. *Reference*, as a form of writing, is well understood; it's used in distinctions we make about writing from an early age.
  旧 | 大多数时候，很容易识别面对的是哪一种。 *参考资料* 作为一种写作形式已广为人知；从很小的时候起，我们便在关于写作的区分中使用它。
  新 | 大体上，要认出面对的是其中的哪一种，并不难。*参考资料*作为一种写作形式，人们早已熟知；我们从小辨别文章体裁时，就会用到它。

  ── [reference-explanation]
  EN | In addition, examples of writing are themselves often clearly one or the other. A tidal chart, with its tables of figures, is clearly reference material. An article that explains *why* there are tides and how they behave is self-evidently explanation.
  旧 | 此外，写作实例本身通常也明显属于某一类。潮汐表及其数值表格显然是参考资料；解释潮汐 *为什么* 产生以及其行为方式的文章，则显然是解释说明。
  新 | 此外，写作的实例本身往往也明显属于其中一类。一张潮汐图，连同它那一张张数字表格，显然属于参考资料；而一篇解释潮汐*为什么*存在、又如何涨落的文章，不言自明就是解释说明。

  ── [reference-explanation]
  EN | There are good rules of thumb:
  旧 | 有一些很好的经验法则：
  新 | 有几条很好的经验法则：

  ── [reference-explanation]
  EN | **If it's boring and unmemorable** it's probably *reference*.
  旧 | **如果它枯燥且难以记住**，那大概就是 *参考资料*。
  新 | **如果它枯燥乏味、让人记不住**，那多半就是*参考资料*。

  ── [reference-explanation]
  EN | **Lists of things** (such as classes or methods or attributes), and **tables of information**, will generally turn out to belong in *reference*.
  旧 | **事物清单** （例如类、方法或属性）和 **信息表格**，通常都属于 *参考资料*。
  新 | **事物清单**（例如类、方法或属性）和**信息表格**，通常都会归入*参考资料*。

  ── [reference-explanation]
  EN | On the other hand **if you can imagine reading something in the bath**, probably, it's *explanation* (even if really there is no accounting for what people might read in the bath).
  旧 | 反之， **如果你能想象在泡澡时阅读某些内容**，那大概是 *解释说明* （尽管人们会在泡澡时读什么，实在无法一概而论）。
  新 | 反过来说，**如果你能想象自己在泡澡时读它**，那它多半就是*解释说明*（尽管人们在泡澡时究竟会读些什么，实在说不准）。

  ── [reference-explanation]
  EN | Imagine asking a friend, while out for a walk or over a drink, **Can you tell me more about <topic>?** - the answer or discussion that follows is most likely going to be an *explanation* of it.
  旧 | 设想你在散步或喝一杯时问朋友： **能否再多讲讲 <topic>？** ——随后的回答或讨论很可能就是对该主题的 *解释说明*。
  新 | 设想你在散步途中或喝一杯的时候，问朋友一句：**能不能多给我讲讲 <topic>？**——随之而来的回答或讨论，多半就是对它的*解释说明*。

  ── [reference-explanation]
  EN | Mostly we can rely safely on intuition to manage the distinction between reference and explanations. But only *mostly* - because it's also quite easy to slip between one form and the other.
  旧 | 大多数时候，我们可放心依靠直觉来区分参考资料和解释说明。但仅仅是 *大多数时候*：因为也很容易从一种形式滑向另一种。
  新 | 大体上，我们尽可以放心靠直觉来分辨参考资料和解释说明。但也只是*大体上*——因为从一种形式滑到另一种，也太容易了。

  ── [reference-explanation]
  EN | It usually happens while writing reference material that starts to become expansive. For example, it's perfectly reasonable to include illustrative examples in reference (just as an encyclopaedia might contain illustrations) - but examples are fun things to develop, and it can be tempting to develop them into explanation (using them to say *why*, or show *what if*, or how it came to be).
  旧 | 这种情况通常发生在撰写逐渐扩展的参考资料时。例如，在参考资料中加入说明性示例完全合理（如同百科全书会包含插图）；但示例很有意思，容易让人将其发展为解释说明（用来说明 *为什么*、展示 *如果怎样*，或解释其如何形成）。
  新 | 这种情况通常发生在参考资料写着写着、开始铺展开来的时候。例如，在参考资料里加入示例完全合理（就像百科全书里也可能有插图）——但示例写起来很好玩，很容易让人忍不住把它写成解释说明（拿它去说*为什么*，去展示*如果……会怎样*，或去说明它是怎么来的）。

  ── [reference-explanation]
  EN | As a result one often finds explanatory material sprinkled into reference. This is bad for the reference, interrupted and obscured by digressions. But it's bad for the explanation too, because it's not allowed to develop appropriately and do its own work.
  旧 | 结果是，参考资料中常常夹杂解释性材料。这对参考资料不利，因为它被旁枝打断和遮蔽；对解释说明也不利，因为它无法得到恰当展开，完成自身的工作。
  新 | 结果是，参考资料里常常星星点点撒着解释性的内容。这对参考资料不利：题外话打断了它，也模糊了它。但这对解释说明同样不利，因为它得不到恰当的展开，做不成自己该做的事。

  ── [reference-explanation]
  EN | The real test, though, if we're in doubt about whether something is supposed to be reference or explanation is: is this something someone would turn to while working, that is, while actually getting something done, executing a task? Or is it something they'd need once they have stepped away from the work, and want to think about it?
  旧 | 不过，若不确定某项内容究竟应是参考资料还是解释说明，真正的检验是：人们会在工作中——也就是实际完成某事、执行任务时——查阅它吗？还是会在离开工作后、想要思考相关内容时才需要它？
  新 | 不过，如果我们拿不准某项内容究竟该算参考资料还是解释说明，真正的检验是：它是人们工作时——也就是实际动手做事、执行任务时——会去查阅的东西吗？还是说，要等他们从工作中抽身出来、想要琢磨琢磨的时候，才会需要它？

  ── [reference-explanation]
  EN | These are two very fundamentally different *needs* of the reader, that reflect how, at that moment, the reader stands in relation to the craft in question, in a relationship of *work* or *study*.
  旧 | 这是读者两种根本不同的 *需求*，反映出读者当下与所涉技艺处于 *工作* 或 *学习* 的关系。
  新 | 这是读者的两种*需求*，从根本上截然不同。这反映出，在那一刻，读者与所涉技艺究竟是*用*还是*学*的关系。

  ── [reference-explanation]
  EN | To help avoid being misled by intuition, see :ref:`compass`.
  旧 | 为避免被直觉误导，请参阅 :ref:`compass`。
  新 | 要想不被直觉误导，请参阅 :ref:`compass`。

  ── [reference-explanation]
  EN | **Reference** is what a user needs in order help *apply* knowledge and skill, while they are working.
  旧 | **参考资料** 是在工作中 *应用* 知识和技能时，用户所需要的内容。
  新 | **参考资料**是用户在工作时*运用（用）*知识和技能所需要的东西。

  ── [reference-explanation]
  EN | **Explanation** is what someone will turn to to help them *acquire* knowledge and skill - "study".
  旧 | **解释说明** 是帮助人们 *习得* 知识和技能——即“学习”——时会查阅的内容。
  新 | **解释说明**是人们为了*习得（学）*知识和技能会去翻阅的东西——“学”。

  ── [reference-explanation]
  EN | Understanding those two relationships and responding to the needs in them is the key to creating effective reference and explanation.
  旧 | 理解这两种关系，并回应其中的需求，是创建有效参考资料和解释说明的关键。
  新 | 理解这两种关系、回应其中的需求，正是创建有效的参考资料和解释说明的关键。
sphinx                     6 条  改动   2

  ── [sphinx]
  EN | <a href="%(path)s">Copyright</a> &#169; %(copyright)s
  旧 | <a href="%(path)s">版权</a> &#169; %(copyright)s
  新 | <a href="%(path)s">版权所有</a> &#169; %(copyright)s

  ── [sphinx]
  EN | Copyright &#169; %(copyright)s
  旧 | 版权 &#169; %(copyright)s
  新 | 版权所有 &#169; %(copyright)s
start-here                78 条  改动  47

  ── [start-here]
  EN | The best way to get started with Diátaxis is by applying it to documentation problems.
  旧 | 开始使用 Diátaxis 的最佳方式，就是把它用到真实的文档问题上去。
  新 | 入门 Diátaxis 的最好办法，就是把它用到文档问题上。

  ── [start-here]
  EN | Start here - Diátaxis in five minutes
  旧 | 从此开始 - 五分钟了解 Diátaxis
  新 | 从这里开始——五分钟了解 Diátaxis

  ── [start-here]
  EN | Treat this website as a handbook or a toolbox that you make use of when you need it.
  旧 | 把本网站当作一份指南或一个工具箱，在你需要时使用。
  新 | 把本网站当作一本手册、一只工具箱，需要时取用。

  ── [start-here]
  EN | You don't need to read everything on this website to make sense of Diátaxis, or to start using it in practice. In fact I recommend that you don't. **The best way to get started with Diátaxis is by applying it** - to something, however small.
  旧 | 理解或在实践中使用 Diátaxis，不需要读完本网站上的所有内容。实际上，我不推荐你这么做。 **入门 Diátaxis 的最好途径，就是去应用它**——应用到某个对象上，无论它多小。
  新 | 要理解 Diátaxis、要在实践中用上它，你都不必读遍本网站的所有内容。其实我建议你别读。**入门 Diátaxis 的最好办法，就是把它用起来**——用在什么东西上都行，多小都行。

  ── [start-here]
  EN | Read this page for a brief primer. Each section contains links to more in-depth material; refer to that when you need it - when you're actually at work, or reflecting on the documentation problems you have encountered.
  旧 | 本页提供简要导读。每个章节均链接到更深入的材料；请在真正开展工作时，或回顾遇到的文档问题时，按需查阅。
  新 | 读读本页，当作一份简明入门。每一节都链接了更深入的材料；需要时再去查阅——在你真正工作的时候，或是在反思自己遇到的文档问题时。

  ── [start-here]
  EN | The core idea of Diátaxis is that there are fundamentally four identifiable kinds of documentation, that respond to four different needs. The four kinds are: *tutorials*, *how-to guides*, *reference* and *explanation*. Each has a different purpose, and needs to be written in a different way.
  旧 | Diátaxis 的核心思想是：从根本上说，文档有四种泾渭分明的类型，它们分别回应四种不同的需求。四种类型是： *教程*， *实践指南*， *参考资料* 和 *解释说明* 。每一种都有不同的目的，撰写方式也各有不同。
  新 | Diátaxis 的核心思想是：文档从根本上说有四种可辨识的类型，回应四种不同的需求。这四种类型是：*教程*、*实践指南*、*参考资料*和*解释说明*。每一种都有不同的目的，也要用不同的方式去写。

  ── [start-here]
  EN | :ref:`Tutorials in more detail <tutorials>`
  旧 | :ref:`教程的更多详细信息 <tutorials>`
  新 | :ref:`教程详解 <tutorials>`

  ── [start-here]
  EN | :ref:`Why tutorials are completely different from how-to guides <tutorials-how-to>`
  旧 | :ref:`为何教程与实践指南截然不同 <tutorials-how-to>`
  新 | :ref:`教程为何与实践指南截然不同 <tutorials-how-to>`

  ── [start-here]
  EN | **A tutorial is a lesson**, that takes a student by the hand through a learning experience. A tutorial is always *practical*: the user *does* something, under the guidance of an instructor. A tutorial is designed around an encounter that the learner can make sense of, in which the instructor is responsible for the learner's safety and success.
  旧 | **教程是一堂课**：它牵着学习者的手，引导其完成一段学习经历。教程始终是 *实践性* 的：用户在讲师的指引下 *亲自动手*。教程应围绕学习者能够理解的体验来设计，讲师要对学习者的安全和成功负责。
  新 | **教程是一堂课**，牵着学生的手，带他走完一段学习经历。教程始终是*实践性*的：用户在讲师的指引下*亲自动手*。教程围绕一次学习者能够理解的相遇来设计，在这次相遇中，讲师要为学习者的安全与成功负责。

  ── [start-here]
  EN | A driving lesson is a good example of a tutorial. The purpose of the lesson is to develop skills and confidence in the student, not to get from A to B. A software example could be: *Let's create a simple game in Python*.
  旧 | 驾驶课是教程的好例子。课程目的在于培养学生的技能和信心，而不是从 A 点到 B 点。软件中的例子可以是： *让我们用 Python 创建一个简单游戏*。
  新 | 驾驶课就是教程的好例子。这堂课的目的，是培养学生的技能与信心，而不是从 A 开到 B。软件领域的例子可以是：*我们用 Python 做一个小游戏*。

  ── [start-here]
  EN | *The user will learn through what they do* - not because someone has tried to teach them.
  旧 | *用户会从亲手所做之事中学习*，而不是因为有人试图教导他们。
  新 | *用户会在自己动手做的过程中学习*——而不是因为有人试图教他们。

  ── [start-here]
  EN | In documentation, the special difficulty is that the instructor is condemned to be absent, and is not there to monitor the learner and correct their mistakes. The instructor must somehow find a way to be present through written instruction alone.
  旧 | 文档的特殊困难在于讲师注定缺席，无法在场观察学习者或纠正其错误。讲师必须设法只靠书面说明来呈现自己。
  新 | 在文档中，特殊的困难在于：讲师注定缺席，无法在场观察学习者、纠正他们的错误。讲师必须设法仅凭书面讲解，让自己仍然在场。

  ── [start-here]
  EN | **A how-to guide addresses a real-world goal or problem**, by providing practical directions to help the user who is in that situation.
  旧 | **实践指南面向现实世界中的目标或问题**，通过提供实用的操作指引，帮助身处相应情境的用户。
  新 | **实践指南面向现实世界中的目标或问题**，给出切实可行的指引，帮助身处那种情境的用户。

  ── [start-here]
  EN | A how-to guide always addresses an already-competent user, who is expected to be able to use the guide to help them get their work done. In contrast to a tutorial, a how-to guide is concerned with *work* rather than *study*.
  旧 | 实践指南总是面向已经具备相应能力的用户，他们应当能够借助它来完成自己的工作。与教程相比，实践指南关注的是 *工作*，而不是 *学习*。
  新 | 实践指南总是面向已经具备相应能力的用户，他们理应能借助这份指南完成自己的工作。与教程不同，实践指南关心的是*工作*，而不是*学习*。

  ── [start-here]
  EN | A how-to guide might be: *How to store cellulose nitrate film* (in motion picture photography) or *How to configure frame profiling* (in software). Or even: *Troubleshooting deployment problems*.
  旧 | 实践指南可以是： *如何保存硝酸纤维素胶片* （电影摄影），或 *如何配置帧性能分析* （软件）。也可以是： *排查部署问题*。
  新 | 实践指南可能是：*如何保存硝酸纤维素胶片*（电影摄影），或者*如何配置帧性能分析*（软件）。甚至可能是：*排查部署问题*。

  ── [start-here]
  EN | **Reference guides contain the technical description** - facts - that a user needs in order to do things correctly: accurate, complete, reliable information, free of distraction and interpretation. They contain *propositional or theoretical knowledge*, not guides to action.
  旧 | **参考资料包含技术描述** ——即用户为正确完成工作所需的事实：准确、完整、可靠，不夹带干扰或阐释的信息。它传递的是 *命题性或理论性知识*，而不是行动指引。
  新 | **参考资料包含技术描述**——即事实——也就是用户要把事情做对所需要的东西：准确、完整、可靠的信息，不夹带干扰，也不夹带阐释。它承载的是*命题性或理论性知识*，而不是行动指南。

  ── [start-here]
  EN | Like a how-to guide, reference documentation serves the user who is at *work*, and it's up to the user to be sufficiently competent to interpret and use it correctly.
  旧 | 和实践指南一样，参考资料服务于正在 *工作* 的用户；用户需自行具备足够能力来正确理解和使用它。
  新 | 和实践指南一样，参考资料服务于处于*工作*状态的用户；能否正确解读并使用它，全看用户自己是否足够胜任。

  ── [start-here]
  EN | *Reference material is neutral.* It is not concerned with what the user is doing. A marine chart could be used by a ship's navigator to plot a course, but equally well by an investigating judge.
  旧 | *参考资料是中立的。* 它不关心用户正在做什么。航海图可以供船舶领航员规划航线，也同样可以供调查法官使用。
  新 | *参考资料是中立的。*它不关心用户正在做什么。航海图可以供船上的领航员规划航线，也同样可以供调查法官使用。

  ── [start-here]
  EN | Where possible, the architecture of reference documentation should reflect the structure or architecture of the thing it's describing - just like a map does. If a method is part of a class that belongs to a certain module, then we should expect to see the same relationship in the documentation too.
  旧 | 在可能的情况下，参考资料的架构应反映其所描述对象的结构或架构，如同地图一般。如果某个方法属于某个类，而该类属于特定模块，文档中也理应呈现同样的关系。
  新 | 只要可能，参考资料的架构就应当反映它所描述之物的结构或架构——就像地图那样。如果一个方法属于某个类，而这个类又属于某个模块，那么在文档中，我们也应当看到同样的关系。

  ── [start-here]
  EN | **Explanatory guides provide context and background.** They serve the need to understand and put things in a bigger picture. Explanation joins things together, and helps answer the question *why?*
  旧 | **解释说明提供语境和背景。** 它服务于人们理解事物、并将其置于更宏大图景之中的需要。解释说明把各个要素联结起来，帮助回答 *为什么？*
  新 | **解释说明提供语境与背景。**它的用处，是帮人理解事物，把事物放进更大的图景里。解释说明把事物联结起来，帮助回答*为什么？*这个问题。

  ── [start-here]
  EN | Explanation often needs to circle around its subject, and approach it from different directions. It can contain opinions and take perspectives.
  旧 | 解释说明往往需要环绕主题，从不同方向切入；它可以包含观点，也可以采取某种立场。
  新 | 解释说明往往需要围绕主题盘旋，从不同方向切入。它可以包含观点，也可以采取不同的视角。

  ── [start-here]
  EN | Like reference, explanation belongs to the realm of propositional knowledge rather than action. However its purpose is to serve the user's study - as tutorials do - and not their work.
  旧 | 与参考资料一样，解释说明属于命题性知识而非行动的领域。不过它服务的是用户的 *学习* ——如同教程——而不是工作。
  新 | 与参考资料一样，解释说明属于命题性知识的领域，而非行动。但它的目的在于服务用户的学习——如同教程那样——而不是用户的工作。

  ── [start-here]
  EN | Often, writers of tutorials who are anxious that their students should *know* things overload their tutorials with distracting and unhelpful explanation. It would be much more useful to give the learner the most minimal explanation ("Here, we use HTTPS because it's safer") and then link to an in-depth article (*Secure communication using HTTPS encryption*) for when the user is ready for it.
  旧 | 教程作者常因担心学生应当 *掌握* 知识，而往教程里塞满分散注意力、毫无助益的解释。更好的做法是先给学习者最精简的说明（“这里使用 HTTPS，因为它更安全”），再链接一篇深入文章（ *使用 HTTPS 加密进行安全通信*），等用户准备好时再读。
  新 | 教程作者常担心学生不*知道*某些东西，于是往教程里塞满分散注意力、毫无助益的解释。远为有用的做法，是先给学习者最精简的解释（“这里用 HTTPS，因为它更安全”），再链接一篇深入的文章（*使用 HTTPS 加密的安全通信*），等用户准备好时再去读。

  ── [start-here]
  EN | The four kinds of documentation and the relationships between them can be summarised in the Diátaxis map.
  旧 | 四类文档及其相互关系，可以用 Diátaxis 地图概括。地图有两个维度：知（认知）与行（行动）；学（习得）与用（应用）。
  新 | 四类文档及其相互关系，可以用 Diátaxis 地图来概括。

  ── [start-here]
  EN | Diátaxis is not just a list of four different things, but a conceptual arrangement of them. It shows how the four kinds of documentation are related to each other, and distinct from each other.
  旧 | Diátaxis 不只是四种事物的清单，更是对它们的概念化组织。它展示四类文档如何彼此关联，又如何相互区分。
  新 | Diátaxis 不只是四种不同东西的清单，更是对它们的概念性排布。它展示了四类文档彼此之间如何关联、又如何区分。

  ── [start-here]
  EN | tutorials and how-to guides are concerned with what the user *does* (**action**)
  旧 | 教程和实践指南关注用户 *做什么*，属于 **行（行动）**
  新 | 教程和实践指南，关注的是用户*做什么*（**行（行动）**）

  ── [start-here]
  EN | reference and explanation are about what the user *knows* (**cognition**)
  旧 | 参考资料和解释说明关注用户 *知道什么*，属于 **知（认知）**
  新 | 参考资料和解释说明，关注的是用户*知道什么*（**知（认知）**）

  ── [start-here]
  EN | tutorials and explanation serve the *acquisition* of skill (the user's **study**)
  旧 | 教程和解释说明服务于技能的习得，即 **学** （用户的 *学习*）
  新 | 教程和解释说明，服务于技能的*习得*（用户的**学**）

  ── [start-here]
  EN | how-to guides and reference serve the *application* of skill (the user's **work**)
  旧 | 实践指南和参考资料服务于技能的应用，即 **用** （用户的 *工作*）
  新 | 实践指南和参考资料，服务于技能的*应用*（用户的**用**）

  ── [start-here]
  EN | But a map doesn't tell you what to *do* - it's reference. To guide your action you need a different sort of tool, in this case, a kind of Diátaxis compass.
  旧 | 但地图不会告诉你该 *怎么做*——它本身就是参考资料。要引导行动，你需要另一种工具；在这里，它就是一种 Diátaxis 指南针。
  新 | 但地图不会告诉你该*怎么做*——它本身就是参考资料。要引导行动，你需要另一种工具；在这里，也就是一种 Diátaxis 指南针。

  ── [start-here]
  EN | When creating documentation, it helps clarify your own intentions, and helps make sure you're actually doing what you think you're doing.
  旧 | 创建文档时，它能帮你厘清自己的意图，并确认自己确实在做自认为正在做的事。
  新 | 创建文档时，它能帮你厘清自己的意图，也能帮你确认：你做的，确实就是你以为自己在做的事。

  ── [start-here]
  EN | When looking at documentation, it helps understand what's going on in it, and makes problems stand out.
  旧 | 审视文档时，它能帮你理解其中的状况，并让问题显现出来。
  新 | 审视文档时，它能帮你理解其中的状况，并让问题凸显出来。

  ── [start-here]
  EN | The compass is not nearly as eye-catching as the map, but when you're at work puzzling over a documentation problem it's what will help you move forward.
  旧 | 指南针远不如地图醒目，但当你正在工作、为文档问题苦思时，正是它能助你继续向前。
  新 | 指南针远不如地图醒目，但当你在工作中为一个文档问题苦苦琢磨时，能让你往前走的，正是它。

  ── [start-here]
  EN | acquisition of skill
  旧 | 技能习得（学）
  新 | 技能的习得（学）

  ── [start-here]
  EN | application of skill
  旧 | 技能应用（用）
  新 | 技能的应用（用）

  ── [start-here]
  EN | Working
  旧 | 实践
  新 | 动手做

  ── [start-here]
  EN | There is a very simple workflow for Diátaxis.
  旧 | Diátaxis 有一个十分简单的工作流程。
  新 | Diátaxis 有一套十分简单的工作流程。

  ── [start-here]
  EN | Consider what you see in the documentation, in front of you right now (which might be literally nothing, if you haven't started yet).
  旧 | 思考一下你眼前此刻的文档内容（如果你还没开始动笔，它或许真的什么也没有）。
  新 | 想一想你此刻在眼前的文档中看到了什么（如果你还没开始，那可能真的什么也没有）。

  ── [start-here]
  EN | Ask: *is there any way in which it could be improved?*
  旧 | 问一问： *有没有什么方式能让它变得更好？*
  新 | 问一问：*有没有什么办法能让它变得更好？*

  ── [start-here]
  EN | Decide on *one* thing you could do to it right now, however small, that would improve it.
  旧 | 决定此刻可以做的 *一件* 事，无论多小，能令文档有所改进即可。
  新 | 定下此刻就能对它做的*一件*事，无论多小，只要能改进它就好。

  ── [start-here]
  EN | And then repeat.
  旧 | 然后重复。
  新 | 然后再重复。

  ── [start-here]
  EN | Do what you like
  旧 | 按你自己的方式来
  新 | 随你所用

  ── [start-here]
  EN | You can do what you like with Diátaxis. You don't have to believe in it and there is no exam. It is a wholly pragmatic approach. I think it's *true*, but what matters is that it actually helps people create better documentation. If you find one idea or insight in it that seems to be worthwhile, help yourself to that.
  旧 | 你可以按自己喜欢的方式使用 Diátaxis。你不必相信它，也没有考试。这是一种完全务实的方法。我认为它是 *正确的*，但重要的是它确实帮助人们创建更好的文档。如果其中有一个想法或洞见对你有价值，尽管拿去使用。
  新 | Diátaxis，你想怎么用就怎么用。你不必相信它，也没有考试。它完全是一种务实的方法。我认为它是*对的*，但真正要紧的是，它确实能帮人写出更好的文档。如果你在其中发现一个看起来有价值的想法或洞见，尽管拿去用。

  ── [start-here]
  EN | There is an extensively elaborated theory around Diátaxis, but you don't need to subscribe to it, or even read about it. Diátaxis doesn't require a commitment to pursue it to a final end.
  旧 | Diátaxis 背后有一套充分展开的理论，但你无需认同它，甚至不必阅读它。Diátaxis 不要求你承诺把它贯彻到底。
  新 | Diátaxis 背后有一套阐发详尽的理论，但你无须认同它，甚至无须去读。Diátaxis 不要求你承诺把它贯彻到底。

  ── [start-here]
  EN | You can do just one thing, right now, and even if you do nothing else ever after, you will at least have made that one improvement. (In practice what you will find is that each thing you do will give you a clue as to the next thing to do - you only need to keep doing them.)
  旧 | 此刻你只需做一件事；即使此后再也不做别的，至少也已经完成了这一项改进。（实践中会发现，每一件完成的事都会为下一件事提供线索——你只要持续去做即可。）
  新 | 此刻，你只做一件事就行；哪怕此后再也不做别的，至少也已经做成了这一项改进。（实践中你会发现：每做一件事，都会带来下一件事的线索——你只需要一直做下去。）

  ── [start-here]
  EN | At this point, you have read everything you need to get started with Diátaxis.
  旧 | 到这里，你已经读完开始使用 Diátaxis 所需的全部内容。
  新 | 到这里，你已经读完了入门 Diátaxis 所需的全部内容。

  ── [start-here]
  EN | You can read more if you want, and eventually you probably should, but *you will get the most value from the guidance in this website when you turn to it with a problem or a question*. That's when it comes alive.
  旧 | 如果愿意，可以继续阅读；最终你或许也应该如此。不过， *当你带着问题或疑问来查阅本网站的指引时，最能从中受益*。那时它才真正鲜活起来。
  新 | 你愿意的话，可以接着往下读——早晚你大概也该读。不过，*当你带着一个问题或疑问来查阅本网站的指引时，你会从中获得最大的价值*。也就是在那一刻，它才真正活了过来。
theory                    15 条  改动   8

  ── [theory]
  EN | The pages in this section are intended to provide some theoretical grounding for the practices Diátaxis prescribes, and to explore some of the questions it raises.
  旧 | 本节页面旨在为 Diátaxis 所倡导的实践提供一些理论基础，并探讨它引出的若干问题。
  新 | 本节各页，意在为 Diátaxis 所主张的实践提供一些理论依据，并探讨它引出的若干问题。

  ── [theory]
  EN | Within the discipline of documentation, discourse tends towards the practical and concrete. The approach is generally heuristic: guidelines, rules of thumb, specific imperatives, principles that we know work.
  旧 | 在文档这一专业领域中，讨论往往偏向实用和具体。通常采用启发式方法：指引、经验法则、具体命令，以及我们已知有效的原则。
  新 | 在文档这一专业领域里，讨论往往偏向务实而具体。方法大体是启发式的：准则、经验法则、具体的硬性要求、我们确知管用的原则。

  ── [theory]
  EN | As practitioners, we have much to say about what to do, and how to do it and how it works, and relatively little to say about *why* it works. Our sense of the right way to do things is largely based on a combination of intuition and experience. The theoretical aspect of the discipline receives far less attention.
  旧 | 作为实践者，我们对做什么、如何做以及它如何起作用有很多可说的，但对它 *为什么* 起作用谈得相对很少。对于正确做事方式的判断，很大程度建立在直觉与经验的结合上。这一专业的理论层面受到的关注要少得多。
  新 | 作为实践者，做什么、怎么做、它如何起作用，我们有很多话可说；它*为什么*有效，却说得相对很少。怎样做才对，我们的判断大半来自直觉与经验的结合。这门学科的理论层面，受到的关注要少得多。

  ── [theory]
  EN | Diátaxis aims to place documentation practice on a more rigorous theoretical footing.
  旧 | Diátaxis 旨在为文档实践奠定更严谨的理论基础。
  新 | Diátaxis 力图让文档实践立足于更严谨的理论根基。

  ── [theory]
  EN | These pages dig deeper into the thinking that underpins Diátaxis.
  旧 | 这些页面更深入地探讨支撑 Diátaxis 的思考。
  新 | 这些页面更深入地挖掘支撑 Diátaxis 的思想。

  ── [theory]
  EN | :doc:`foundations` - *why* Diátaxis works
  旧 | :doc:`foundations` ——Diátaxis *为什么* 有效
  新 | :doc:`foundations`——Diátaxis *为什么*有效

  ── [theory]
  EN | :doc:`map` - documentation in two dimensions
  旧 | :doc:`map` ——二维的文档
  新 | :doc:`map`——文档的两个维度

  ── [theory]
  EN | Common problems explored:
  旧 | 所探讨的常见问题：
  新 | 常见问题探讨：
translation               34 条  改动  23

  ── [translation]
  EN | If you'd like to help translate Diátaxis into your language, that would be very welcome.
  旧 | 如果愿意帮助将 Diátaxis 翻译成你的语言，我们非常欢迎。
  新 | 如果你愿意帮忙把 Diátaxis 翻译成你的语言，那将非常受欢迎。

  ── [translation]
  EN | As soon as a translation is complete, I will publish it on https://diataxis.fr.
  旧 | 翻译一完成，我就会将其发布到 https://diataxis.fr。
  新 | 译文一完成，我就会把它发布到 https://diataxis.fr。

  ── [translation]
  EN | The best way to contribute to translation is via `Transifex <https://transifex.com>`_, where you'll need an account.
  旧 | 参与翻译的最佳方式是使用 `Transifex <https://transifex.com>`_，你需要在该平台拥有账号。
  新 | 参与翻译最好的办法是上 `Transifex <https://transifex.com>`_，你需要在那里注册一个账号。

  ── [translation]
  EN | Go to the `Diátaxis page on Transifex <https://explore.transifex.com/danieleprocida/diataxis/>`_, and select `Join this project <https://app.transifex.com/join/?o=danieleprocida&p=diataxis&t=opensource>`_.
  旧 | 前往 `Transifex 上的 Diátaxis 页面 <https://explore.transifex.com/danieleprocida/diataxis/>`_，并选择 `加入此项目 <https://app.transifex.com/join/?o=danieleprocida&p=diataxis&t=opensource>`_。
  新 | 前往 `Transifex 上的 Diátaxis 页面 <https://explore.transifex.com/danieleprocida/diataxis/>`_，再选择`加入此项目 <https://app.transifex.com/join/?o=danieleprocida&p=diataxis&t=opensource>`_。

  ── [translation]
  EN | There you'll find the option to join the translation team for the language you're interested in. After that I will receive notification of your join request, and will add you to the team. Your own `Transifex dashboard <https://app.transifex.com/home/>`_ will remain blank until I do.
  旧 | 在那里可以选择加入所感兴趣语言的翻译团队。之后我会收到你的加入请求通知，并将你加入团队。在此之前，你自己的 `Transifex 控制面板 <https://app.transifex.com/home/>`_ 会保持空白。
  新 | 在那里，你会看到加入自己感兴趣语言翻译团队的选项。之后我会收到你的加入请求通知，然后把你加进团队。在我把你加进去之前，你自己的 `Transifex 控制面板 <https://app.transifex.com/home/>`_ 会一直是空的。

  ── [translation]
  EN | By all means email me to let me know, because the Transifex notifications don't come in immediately.
  旧 | 也欢迎给我发邮件告知，因为 Transifex 的通知不会立即送达。
  新 | 请尽管给我发邮件说一声，因为 Transifex 的通知不是马上就到。

  ── [translation]
  EN | Once you've been added to the team, you'll see an overview of the available languages. You can see all of them, but can only translate the one whose team you're in.
  旧 | 加入团队后，你会看到可用语言的概览。可以查看所有语言，但只能翻译自己所属团队的语言。
  新 | 加入团队后，你会看到可用语言的概览。所有语言你都看得见，但只能翻译你所在团队的那一种。

  ── [translation]
  EN | References and file names
  旧 | 引用和文件名
  新 | 参考和文件名

  ── [translation]
  EN | Don't translate names of files or Sphinx references. For example, if you see the string ``:doc:`tutorials` - learning-oriented experiences`` you need to leave ``tutorials`` as it is.
  旧 | 不要翻译文件名或 Sphinx 引用。例如，若看到字符串 ``:doc:`tutorials` - learning-oriented experiences``，必须保持 ``tutorials`` 不变。
  新 | 不要翻译文件名，也不要翻译 Sphinx 参考。例如，如果看到字符串 ``:doc:`tutorials` - learning-oriented experiences``，就必须把 ``tutorials`` 原样保留。

  ── [translation]
  EN | Right now page URLs are *not* being translated, so the French page for *Tutoriels* will be at https://diataxis-translated.readthedocs.io/fr/tutorials/.
  旧 | 目前页面 URL *不会* 翻译，因此法语的 *Tutoriels* 页面地址会是 https://diataxis-translated.readthedocs.io/fr/tutorials/。
  新 | 目前页面 URL *不会*翻译，所以法语的教程页面 *Tutoriels* 会位于 https://diataxis-translated.readthedocs.io/fr/tutorials/。

  ── [translation]
  EN | That's not very elegant, but at this stage I don't know if there is an alternative.
  旧 | 这并不十分优雅，但现阶段我不知道是否有替代方案。
  新 | 这算不上多优雅，但现阶段我不知道还有没有别的办法。

  ── [translation]
  EN | In Transifex you will sometimes see `numbered placeholder symbols <https://help.transifex.com/en/articles/6240403-translating-html-content>`_ for functional Sphinx references. Your translation should include the placeholders too.
  旧 | 在 Transifex 中，有时会看到用于功能性 Sphinx 引用的 `带编号占位符 <https://help.transifex.com/en/articles/6240403-translating-html-content>`_。译文中也应保留这些占位符。
  新 | 在 Transifex 里，你有时会看到 Sphinx 功能性参考的`带编号的占位符 <https://help.transifex.com/en/articles/6240403-translating-html-content>`_。你的译文也应当包含这些占位符。

  ── [translation]
  EN | **The first page to translate** (Transifex calls pages "resources) for a new language should be *Start here*. It should also be the first one to refer to if you're contributing to an existing language.
  旧 | 新语言 **第一个要翻译的页面** （Transifex 将页面称为“资源”）应是 *从此开始*。为已有语言贡献时，也应优先参照该页面。
  新 | 一门新语言**第一个要翻译的页面**（Transifex 把页面叫作“资源”），应当是*从这里开始*。如果你是在给已有语言做贡献，它也应当是你首先要参照的页面。

  ── [translation]
  EN | The reason for that is that it covers the whole of Diátaxis in one page, and gathers together almost all the special terms and forms of words that you will encounter elsewhere. It should be a good guide to translation decisions in general.
  旧 | 原因在于，它在一页中涵盖整个 Diátaxis，并汇集了几乎所有会在其他地方遇到的专用术语和词形。它应能为一般的翻译决策提供良好指引。
  新 | 因为它以一页篇幅覆盖了整个 Diátaxis，把你在别处会遇到的专用术语和词形几乎都收了进来。总的来说，它应当能很好地指引翻译取舍。

  ── [translation]
  EN | I prefer translations to contain good translations for key terms **in their own language**. Even if it's common to use the English term "how-to" in your language, I don't want the translations to do that. They should find a native alternative, and use it consistently.
  旧 | 我希望译文能用 **目标语言自身** 恰当地翻译关键术语。即使你的语言中常用英文 “how-to”，我也不希望译文这样做；应找到本族语的替代说法，并一致使用。
  新 | 我希望译文能为关键术语给出**用目标语言本身**写就的好译法。即使你的语言里常说英文的“how-to”，我也不希望译文照搬。应当找到本族语的说法，并一直用它。

  ── [translation]
  EN | I care much more about **the meaning and force of the ideas** in Diátaxis than the preservation of the way I have expressed them in English. I certainly don't want or expect literal translation. Translations should be idiomatic and sound unforced. Use native sentence structures and constructions. If better metaphors or turns of phrase exist in your language, use those. I'll be happy to discuss those questions.
  旧 | 与保留我用英语表达的方式相比，我更在意 Diátaxis 中 **思想的含义和力度**。我当然不想要、也不期待逐字翻译。译文应符合语言习惯、读来不显生硬；请使用本族语的句式和结构。若你的语言中有更好的隐喻或措辞，请用它们。我很乐意讨论这些问题。
  新 | 比起保留我在英语里的表达方式，我更在意 Diátaxis 里**思想的含义与力度**。我当然不要、也不指望逐字翻译。译文应当地道，读来不显生硬。要用本族语的句式和构造。如果你的语言里有更好的比喻或说法，就用它们。我很乐意讨论这些问题。

  ── [translation]
  EN | **Take note of the bigger picture.** When you're looking at string by string translations, it's easy to acquire tunnel vision and lose awareness of the context.
  旧 | **留意整体图景。** 逐条查看字符串译文时，很容易视野变得狭窄，只见树木不见森林，失去对语境的感知。
  新 | **要留意更大的图景。**一条条看译文时，人很容易只见树木，不见森林，失去对语境的把握。

  ── [translation]
  EN | I expect that translation will be collaborative work involving multiple translators, not all of whom might agree on how to translate a particular string.
  旧 | 我预计翻译将是一项涉及多位译者的协作工作，未必所有人都会同意某条字符串应如何翻译。
  新 | 我预期翻译会是由多位译者协作完成的工作，而他们未必都同意某条字符串该怎么译。

  ── [translation]
  EN | If you see something that's clearly wrong (spelling, grammar, punctuation, lost meaning, unidiomatic rendering) correct it.
  旧 | 如果看到明显错误（拼写、语法、标点、意思丢失或表达不地道），请修正它。
  新 | 看到明显错误（拼写、语法、标点、原意丢失、译文不地道），就改掉它。

  ── [translation]
  EN | Translation contributions are accepted under the `Creative Commons Attribution-ShareAlike 4.0 International Public License <https://github.com/evildmp/diataxis-documentation-framework/blob/main/LICENSE.rst>`_.
  旧 | 翻译贡献采用 `知识共享 署名-相同方式共享 4.0 国际许可协议 <https://github.com/evildmp/diataxis-documentation-framework/blob/main/LICENSE.rst>`_。
  新 | 翻译贡献均按`知识共享 署名-相同方式共享 4.0 国际许可协议 <https://github.com/evildmp/diataxis-documentation-framework/blob/main/LICENSE.rst>`_ 接受。

  ── [translation]
  EN | Translation is in progress for various other languages, including French, Italian, Portuguese (Brazil), Chinese (Simplified), Korean and Japanese. Others can be added on request and will be published there when more translations are added.
  旧 | 其他多种语言的翻译也在进行中，包括法语、意大利语、葡萄牙语（巴西）、简体中文、韩语和日语。可根据请求添加其他语言；有更多译文时，也会在那里发布。
  新 | 另有多种语言的翻译也在进行中，包括法语、意大利语、葡萄牙语（巴西）、简体中文、韩语和日语。其他语言可以按要求添加；等译文再多一些，它们也会发布到那里。

  ── [translation]
  EN | Translation takes place page by page and then string by string - little fragments of the overall text. When you save a translation string, it's marked as translated. I get notifications of these, and periodically I'll pull them down into the repository and publish a new version of the site containing them.
  旧 | 翻译先逐页进行，再逐条处理字符串，也就是整篇文本中的小片段。保存一条译文后，它会被标记为已翻译。我会收到通知，并定期将译文拉取到代码仓库，发布包含这些译文的新网站版本。
  新 | 翻译先逐页来，再逐条字符串来——那是整篇文本的零星片段。一条译文保存后，就会标记为已翻译。我会收到这些通知，并定期把译文拉进代码仓库，发布一个包含这些译文的新版网站。

  ── [translation]
  EN | If it's more complex, and seems like a stylistic choice or a question of judgement, it would be good to discuss it first. There is a `Transifex forum for this project <https://app.transifex.com/danieleprocida/teams/120528/discussions/>`_, or you can raise the question with me.
  旧 | 如果情况更复杂，像是风格选择或判断问题，最好先讨论。项目有一个 `Transifex 论坛 <https://app.transifex.com/danieleprocida/teams/120528/discussions/>`_，你也可以向我提出问题。
  新 | 如果情况更复杂，像是一个风格取舍或见仁见智的问题，最好先讨论一下。本项目有一个 `Transifex 论坛 <https://app.transifex.com/danieleprocida/teams/120528/discussions/>`_，你也可以向我提出这个问题。
tutorials                107 条  改动  92

  ── [tutorials]
  EN | A tutorial is an **experience** that takes place under the guidance of a tutor. A tutorial is always **learning-oriented**.
  旧 | 教程是在导师指导下进行的一种 **体验**。教程始终 **以学习为导向**。
  新 | **体验**——教程是在导师指导下展开的一段经历。教程永远是**面向学习**的。

  ── [tutorials]
  EN | A tutorial is a *practical activity*, in which the student learns by doing something meaningful, towards some achievable goal.
  旧 | 教程是一种 *实践活动*，学生在其中通过完成某项有意义的任务来学习，以达成某些可实现的目标。
  新 | 教程是一种*实践活动*：学生在其中通过动手做一件有意义的事来学习，朝着某个可以达到的目标前进。

  ── [tutorials]
  EN | A tutorial serves the user's *acquisition* of skills and knowledge - their study. Its purpose is not to help the user get something done, but to help them learn.
  旧 | 教程服务于 **学（习得）**——即用户对技能和知识的学习。它的目的不是帮助用户完成任务，而是帮助他们学习。
  新 | 教程服务于用户对技能与知识的*习得*，也就是他们的学习。它的目的不是帮用户把某件事做成，而是帮他们学习。

  ── [tutorials]
  EN | Tutorials - learning-oriented guides that describe practical steps and are intended to serve our study.
  旧 | 教程——以学习为导向，通过实际操作步骤（行）服务于技能习得（学）的指南。
  新 | 教程——面向学习、描述实操步骤的指南，意在服务于我们的学习（学）。

  ── [tutorials]
  EN | It's important to understand that while a student will learn by doing, what the student *does* is not necessarily what they *learn*. Through doing, they will acquire theoretical knowledge (i.e. facts), understanding, familiarity. They will learn how things relate to each other and interact, and how to interact with them. They will learn the names of things, the use of tools, workflows, concepts, commands. And so on.
  旧 | 重要的是要明白：虽然学生是动手学会的，但他们 *做的* 并不一定就是他们 *学到的*。通过动手，他们会获得理论知识（即事实）、理解和熟悉感；他们会了解事物之间如何关联、如何相互作用，以及如何与它们打交道；他们会记住事物的名称，学会使用工具、工作流程、概念和命令，等等。
  新 | 有一点要明白：学生固然是动手学会的，但他们*做*的事，未必就是他们*学到*的东西。通过动手，他们会获得理论知识（也就是事实）、理解和熟悉感。他们会了解事物之间如何关联、如何相互作用，也会了解如何与它们打交道。他们会知道事物的名称，学会使用工具、工作流程、概念、命令。诸如此类。

  ── [tutorials]
  EN | A lesson entails a relationship between a teacher and a pupil. In all learning of this kind, *learning takes place as the pupil applies themself to tasks under the instructor's guidance*.
  旧 | 一堂课意味着教师与学生之间存在一种关系。在所有这类学习中， *学生只有在导师指导下投身各项任务，学习才会真正发生*。
  新 | 一堂课意味着教师与学生之间存在一种关系。在所有这类学习中，*学生只有在导师指导下投身各项任务，学习才会真正发生*。

  ── [tutorials]
  EN | A lesson is a *learning experience*. In a learning experience, what matters is what the learner does and what happens. By contrast, the teacher's explanations and recitations of fact are far less important.
  旧 | 一堂课是一种 *学习体验*。在学习体验中，重要的是学习者做了什么以及发生了什么事。相比之下，教师的解释和事实复述则远不那么重要。
  新 | 一堂课是一种*学习体验*。在学习体验里，要紧的是学习者做了什么、发生了什么。相比之下，教师的解释和对事实的复述则远没有那么重要。

  ── [tutorials]
  EN | A good lesson gives the learner confidence, by showing them that they can be successful in a certain skill or with a certain product.
  旧 | 一堂好课通过向学习者展示他们能在某项技能或某个产品上取得成功，来给他们带来自信。
  新 | 一堂好课给学习者信心——让他们看到，自己能在某项技能或某个产品上获得成功。

  ── [tutorials]
  EN | It's not easy being a teacher.
  旧 | 为人师表绝非易事。
  新 | 当教师绝非易事。

  ── [tutorials]
  EN | A lesson is a kind of contract between teacher and student, in which nearly all the responsibility falls upon the teacher. The teacher has responsibility for what the pupil is to learn, what the pupil will do in order to learn it, and for the pupil's success. Meanwhile, the only responsibility of the pupil in this contract is to be attentive and to follow the teacher's directions as closely as they can. There is no responsibility on the pupil to learn, understand or remember.
  旧 | 一堂课是教师与学生之间的一种契约，其中几乎所有的责任都落在教师身上。教师对学生将要学习的内容、为学习该内容而需进行的活动以及学生的成功负有责任。与此同时，在该契约中，学生唯一需要承担的责任是保持专注并尽可能严格地遵循教师的指示。学生并无学习、理解或记住的责任。
  新 | 一堂课是教师与学生之间的一种契约，几乎所有责任都落在教师身上。学生要学什么、为学会它要做什么、以及学生能否成功，都是教师的责任。而在这份契约里，学生唯一的责任就是专心，并尽可能严格地照教师的指示去做。学生没有学习、理解或记住的责任。

  ── [tutorials]
  EN | At the same time, the exercise you put your pupils through must be:
  旧 | 同时，你让学生经历的练习必须是：
  新 | 与此同时，你让学生经历的练习必须是：

  ── [tutorials]
  EN | *meaningful* - the pupil needs to have a sense of achievement
  旧 | *有意义的* ——学生需要有一种成就感
  新 | *有意义的*——学生需要有一种成就感

  ── [tutorials]
  EN | *successful* - the pupil needs to be able to complete it
  旧 | *成功的* ——学生需要能够完成它
  新 | *成功的*——学生需要能够完成它

  ── [tutorials]
  EN | *logical* - the path that the pupil takes through it needs to make sense
  旧 | *符合逻辑* ——学习者所走的路径必须合乎逻辑
  新 | *符合逻辑*——学生所走的路径必须说得通

  ── [tutorials]
  EN | *usefully complete* - the pupil must have an encounter with all of the actions, concepts and tools they need to become familiar with
  旧 | *具有实用完整性* ——学习者必须接触到所有需要熟悉的操作、概念和工具
  新 | *完整而有用*——学生必须接触到所有需要熟悉的行动、概念和工具

  ── [tutorials]
  EN | The problem of tutorials
  旧 | 教程的问题
  新 | 教程的难题

  ── [tutorials]
  EN | Tutorials are rarely done well, partly because they are genuinely difficult to do well, and partly because they are not well understood. In software, many products lack good tutorials, or lack tutorials completely; tutorials are often conflated with how-to guides.
  旧 | 教程很少做得好，部分是因为做好它们确实很难，部分是因为人们对它们的理解不足。在软件领域，许多产品缺少良好的教程，甚至完全没有教程；人们常常将教程与实践指南混为一谈。
  新 | 教程很少做得好，部分是因为要做好它确实很难，部分是因为人们对它理解不足。在软件领域，许多产品缺少好教程，或者干脆没有教程；教程常常与实践指南混为一谈。

  ── [tutorials]
  EN | In an ideal lesson, the teacher is present and interacts with and responds to the student, correcting their mistakes and checking their learning. In documentation, none of this is possible.
  旧 | 在一堂理想的课程中，教师在场并与学生互动、回应学生的提问，纠正其错误并检查其学习进展。而在文档中，这一切都不可能实现。
  新 | 在一堂理想的课上，教师就在现场，与学生互动、回应学生，纠正他们的错误，检查他们的学习。而在文档里，这一切都做不到。

  ── [tutorials]
  EN | Writing and maintaining tutorials can consume a remarkable amount of effort and time.
  旧 | 编写和维护教程需要耗费大量精力和时间。
  新 | 编写和维护教程，会耗掉多得惊人的精力和时间。

  ── [tutorials]
  EN | It's hard enough to put together a learning experience that meets all the standards described above; in many contexts the product itself evolves rapidly, meaning that all that work needs to be done again to ensure that the tutorial still performs its required functions.
  旧 | 要构建符合上述所有标准的学习体验已经十分困难；在许多情境中，产品本身发展迅速，这意味着必须反复重做这些工作，以确保教程仍能履行其应有的功能。
  新 | 要打造一段符合上述所有标准的学习体验，已经够难了；而在很多情境下，产品本身变化飞快，意味着所有这些活儿都得重做一遍，才能保证教程仍然发挥它该有的作用。

  ── [tutorials]
  EN | You will also often find that no other part of your documentation is subject to revisions the way your tutorials are. Elsewhere in documentation, changes and improvements can generally be made discretely; in tutorials, where the end-to-end learning journey must make sense, they often cascade through the entire story.
  旧 | 你还会经常发现，文档中的其他部分并不会像教程那样频繁修订。在文档的其他部分，变更和改进通常可以独立进行；而在教程中，由于端到端的学习旅程必须合乎逻辑，任何改动往往会波及整个故事线。
  新 | 你还常常会发现，文档里没有别的部分像教程那样频繁地修订。文档的其他地方，改动和改进通常可以各改各的；但在教程里，从头到尾的学习旅程必须讲得通，一处改动往往会一路荡开，波及整个故事。

  ── [tutorials]
  EN | Finally, tutorials contain the additional complication of the distinction between *what is to be learned* and *what is to be done*. Not only must the creator of a tutorial have a good sense of what the user must learn, and when, they must also devise a meaningful learning journey that somehow delivers all that.
  旧 | 最后，教程还有一个额外的复杂之处：要在 *该学什么* 与 *该做什么* 之间作出区分。教程的创作者不仅要对用户必须学什么、何时学有清楚的把握，还要设计出一条富有意义的学习旅程，把这一切切实承载起来。
  新 | 最后，教程还多一层麻烦：*要学的是什么*、*要做的是什么*，这两者得区分开。教程的创作者不仅要清楚用户必须学会什么、何时学会，还要设计出一段有意义的学习旅程，把这一切都兜住。

  ── [tutorials]
  EN | It's not an easy problem, but neither is it a mystery. The principles outlined below - repetition, action, small steps, results early and often, concreteness and so on - are not secrets, but they are not always well understood.
  旧 | 这个问题并不简单，但也并非神秘莫测。下文所述的原则——重复、行动、小步递进、尽早且频繁地获得成果、具体化等——并非什么秘密，但它们也常常未被充分理解。
  新 | 它不是个容易的问题，但也并非什么谜团。下文列出的那些原则——重复、行动、小步推进、尽早且频繁地拿到结果、具体化等等——都不是什么秘密，却也没有被普遍理解。

  ── [tutorials]
  EN | Still, there are straightforward, effective ways to address the problems of pedagogy in practice.
  旧 | 然而，在实践中解决教学问题依然存在直接而有效的方法。
  新 | 不过，在实践中解决教学问题，还是有直接而有效的办法。

  ── [tutorials]
  EN | The first rule of teaching is simply: **don't try to teach**. Your job, as a teacher, is to provide the learner with an experience that will allow them to learn. A teacher inevitably feels a kind of anxiety to impart knowledge and understanding, but if you give into it and try to teach by telling and explaining, you will jeopardise the learning experience.
  旧 | **教学的第一条准则很简单：别试图去教。** 你作为教师的职责，是给学习者提供一种能让他们真正学会的体验。教师难免会有一种急于灌输知识和理解的冲动，但如果你放任这种冲动，试图靠讲解来教学，就会毁掉这次学习体验。
  新 | 教学的第一条准则很简单：**别试图去教**。作为教师，你的职责是给学习者一段能让他们学习的体验。教师总会有一种急于传授知识和理解的焦躁，但你一旦屈从于它，想靠讲述和解释来教，就会毁掉这段学习体验。

  ── [tutorials]
  EN | Instead, *allow learning to take place*, and trust that it will. Give your learner things to *do*, through which they can learn. Only your pupil can learn. Sadly, however much you desire it, you will not be able to learn for your pupil. You cannot make them learn. All you can do is make it so *they* can learn.
  旧 | **相反，让学习自然发生**，并相信它会如此。给你的学习者一些 **可做** 的事情，通过这些活动他们可以学习。只有你的学生才能学会知识。遗憾的是，无论多么渴望，你都无法替学生去学习。你不能强制他们学习。你所能做的只是创造条件，让他们 **能够** 学习。
  新 | 相反，*让学习发生*，并相信它自会发生。给学习者一些事情去*做*，让他们从中学习。只有你的学生才能学。遗憾的是，无论你多么渴望，都无法替你的学生去学。你没法让他们学会。你所能做的，只是把学习变成可能；真正学得会的，是*他们*。

  ── [tutorials]
  EN | Show the learner where they'll be going
  旧 | **向学习者展示他们将要去往何处**
  新 | 让学习者知道此行的去向

  ── [tutorials]
  EN | It's important to allow the learner to form an idea of what they will achieve right from the start. As well as helping to set expectations, it allows them to see themselves building towards the completed goal as they work.
  旧 | **从一开始就让学习者形成对自己将达成成果的认识是很重要的**。这不仅有助于设定期望，还使他们能够在工作中看到自己朝着完成的目标逐步迈进。
  新 | 从一开始就让学习者对将要取得的成果有个概念，这很重要。这既有助于建立预期，也让他们在做的过程中看到自己正一步步走向最终的目标。

  ── [tutorials]
  EN | Providing the picture the learner needs in a tutorial can be as simple as informing them at the outset: *In this tutorial we will create and deploy a scalable web application. Along the way we will encounter containerisation tools and services.*
  旧 | **在教程里勾勒学习者所需的图景，可以简单到一开场就告诉他们：**“本教程中，我们将构建并部署一个可扩展的 Web 应用；途中会接触到容器化工具和服务。”
  新 | 在教程里给出学习者需要的那幅图景，可以简单到一开头就告诉他们：*本教程中，我们将创建并部署一个可扩展的 Web 应用。一路上我们会遇到容器化工具与服务。*

  ── [tutorials]
  EN | This is not the same as saying: *In this tutorial you will learn...* - which is presumptuous and a very poor pattern.
  旧 | 这不是在说“在本教程中你将学会……”——那样显得自以为是，是一种很差的做法。
  新 | 这和说这句话不是一回事：*在本教程中你将会学到……*——那样说显得有些自以为是，是一种很糟的套路。

  ── [tutorials]
  EN | Deliver visible results early and often
  旧 | **尽早并频繁地展示可见成果**
  新 | 尽早、频繁地交付可见的成果

  ── [tutorials]
  EN | Your learner is probably doing new and strange things that they don't fully understand. Understanding comes from being able to make connections between causes and effects, so let them see the results and make the connections rapidly and repeatedly. Each one of those results should be something that the user can see as meaningful.
  旧 | 你的学习者可能正在尝试一些新颖且陌生的操作，而他们尚未完全理解。理解源于能够建立因果关系之间的联系，因此要让他们看到结果，并迅速、重复地建立这些联系。每一个结果都应是用户能视为有意义的东西。
  新 | 你的学习者大概正在做一些新奇的、陌生的事情，自己还没完全弄懂。理解来自在因果之间建立联系，所以要让他们看到结果，并迅速、反复地建立这种联系。每一个这样的结果，都应当是用户看得出意义的东西。

  ── [tutorials]
  EN | Every step the learner follows should produce a comprehensible result, however small.
  旧 | 学习者遵循的每一步都应产生一个可理解的结果，无论其多么微小。
  新 | 学习者每走一步，都应当得出一个看得懂的结果，无论多小。

  ── [tutorials]
  EN | Maintain a narrative of the expected
  旧 | 持续叙述预期中的结果
  新 | 持续叙述预期

  ── [tutorials]
  EN | At every step of a tutorial, the user experiences a moment of anxiety: will this action produce the correct result? Part of the work of a successful tutorial is to keep providing feedback to the learner that they are indeed on the right path.
  旧 | 在教程的每一步，用户都会经历一个焦虑的时刻：这个操作会得到正确的结果吗？成功的教程，一部分工作就在于不断向学习者反馈，让他们确信自己正走在正确的路上。
  新 | 教程的每一步，用户都会经历一个焦虑的瞬间：这个行动会产生正确的结果吗？成功的教程，有一部分功夫就花在不断给学习者反馈，让他们确信自己确实走在正确的路上。

  ── [tutorials]
  EN | Keep up a narrative of expectations: "You will notice that ..."; "After a few moments, the server responds with ...". Show the user actual example output, or even the exact expected output.
  旧 | 持续叙述预期：“你将注意到……”；“片刻之后，服务器会返回……”。向用户展示实际的示例输出，甚至精确的预期输出。
  新 | 不断叙述你的预期：“你会注意到……”；“过一会儿，服务器会返回……”。向用户展示真实的示例输出，甚至是精确的预期输出。

  ── [tutorials]
  EN | If you know in advance what the likely signs of going wrong are, consider flagging them: "If the output doesn't show ..., you have probably forgotten to ...".
  旧 | 如果你预先知道可能出现问题的迹象，请考虑对其进行标记："如果输出未显示……，你可能忘记……"。
  新 | 如果你事先知道出错通常会有哪些征兆，不妨把它们标出来：“如果输出里没有显示……，你多半是忘了……”。

  ── [tutorials]
  EN | It's helpful to prepare the user for possibly surprising actions: "The command will probably return several hundred lines of logs in your terminal."
  旧 | 提前让用户对可能出人意料的操作有所准备，会很有帮助："该命令将在你的终端中返回数百行日志。"
  新 | 提前让用户对可能出人意料的操作有个心理准备，会很有帮助：“这条命令大概会在你的终端里返回几百行日志。”

  ── [tutorials]
  EN | Point out what the learner should notice
  旧 | 指出学习者应该注意的内容。
  新 | 指出学习者该注意什么

  ── [tutorials]
  EN | Learning requires reflection. This happens at multiple levels and depths, but one of the first is when the learner  observes the signs in their environment. In a lesson, a learner is typically too focused on what they are doing to notice them, unless they are prompted by the teacher.
  旧 | 学习需要反思。反思发生在多个层面、多种深度，但最早的一层，是学习者留意到周围环境中的种种迹象。在课堂上，学习者通常太专注于手上的事，注意不到这些迹象，除非有老师提示。
  新 | 学习需要反思。反思会在多个层面、多种深度上发生，但最先发生的一层，是学习者留意到周围环境中的种种迹象。在课堂上，学习者通常太专注于手上的事，注意不到这些迹象，除非老师提醒。

  ── [tutorials]
  EN | Your job as teacher is to close the loops of learning by pointing things out, in passing, as the lesson moves along. This can be as simple as pointing out how a command line prompt changes, for example.
  旧 | 作为教师，你要在课程推进中顺带把关键之处点明，让学习形成闭环。这可以简单到比如指出命令行提示符的变化。
  新 | 作为教师，你要在课程推进的过程中顺手指点，把一处处学习回路闭合起来。这可以简单到比如指一下命令行提示符的变化。

  ── [tutorials]
  EN | Observing is an active part of a craft, not a merely passive one. It means paying attention to the environment, a skill in itself. It's often neglected.
  旧 | 观察是技艺的一个积极组成部分，而不仅仅是一种被动的行为。这意味着关注环境，这本身就是一种技能。它经常被忽视。
  新 | 观察是技艺中主动的一环，而非仅仅被动的一环。它意味着对环境保持留意，这本身就是一门技能。而它常常被忽视。

  ── [tutorials]
  EN | Target *the feeling of doing*
  旧 | 以 *行事的感受* 为目标
  新 | 以*行事的感受*为目标

  ── [tutorials]
  EN | In all skill or craft, the accomplished practitioner experiences a *feeling of doing*, a joined-up purpose, action, thinking and result.
  旧 | 在任何技艺中，娴熟的实践者都会体验到一种 *行事的感受*：目的、行动、思考与结果融为一体。
  新 | *行事的感受*——在一切技能、一切技艺中，娴熟的实践者都会体验到它：目的、行动、思考与结果连成一体。

  ── [tutorials]
  EN | As skill develops, it flows in a confident rhythm and becomes a kind of pleasure. It's the pleasure of walking, for example.
  旧 | 随着技艺精进，它会以自信的节奏自然流淌，逐渐成为一种愉悦——比如行走时的那种愉悦。
  新 | 技艺渐长，动作便以自信的节奏流动起来，成为一种愉悦——比如走路的那种愉悦。

  ── [tutorials]
  EN | Pay attention to your own *feeling of doing* in your work. What is it like to perform a particular operation?
  旧 | 留意自己工作时那份 *行事的感受*。执行某个具体操作时，是什么感觉？
  新 | 留意你自己工作时的*行事的感受*。做某个具体操作时，那是什么感觉？

  ── [tutorials]
  EN | Your learner's skill depends upon their discovering this feeling, and its becoming a pleasure.
  旧 | 学习者的技艺，取决于他们能否体会到这种感受，并让它成为一种愉悦。
  新 | 学习者的技艺，取决于他们能否发现这份感受，并让它成为一种愉悦。

  ── [tutorials]
  EN | Your challenge as the creator of a tutorial is to ensure that its tasks tie together purpose and action so they become a cradle for this feeling.
  旧 | 作为教程创作者，你的挑战在于确保教程中的任务能把目的与行动紧密相连，使之成为滋养这种感受的摇篮。
  新 | 作为教程的创作者，你的挑战在于：让教程中的任务把目的与行动系为一体，成为孕育这份感受的摇篮。

  ── [tutorials]
  EN | Encourage and permit repetition
  旧 | 鼓励并允许重复练习
  新 | 鼓励并允许重复

  ── [tutorials]
  EN | Learners will return to and repeat an exercise that gives them success, for the pleasure they find in getting the expected result. Doing so reaffirms to them that they can do it, and that it works.
  旧 | 学习者会愿意反复练习自己能够成功完成的内容，因为得到预期结果会带来愉悦。这会再次确认：他们能够做到，而且方法确实有效。
  新 | 凡是能带来成功的练习，学习者都会一再回头去做，因为拿到预期结果让他们感到愉悦。这样做会再一次向他们确认：他们做得到，而且这办法管用。

  ── [tutorials]
  EN | Repetition is a key to establishing the feeling of doing; being at home with that feeling is a foundational layer of learning.
  旧 | 重复是建立这种行事的感受的关键；对这种感受习以为常，是学习的基石。
  新 | 重复是建立行事的感受的关键；对这份感受习以为常，是学习的基础层。

  ── [tutorials]
  EN | Repetition is not the best teacher - sometimes it's the *only* teacher.
  旧 | 重复并非最好的教师——有时它甚至是唯一的教师。
  新 | 重复并非最好的老师——有时，唯有它才是*唯一的老师*。

  ── [tutorials]
  EN | In your tutorial, try to make it possible for a particular step and result to be repeated. This can be difficult, for example in operations that are not reversible (making it hard to go back to a previous step) - but seek it wherever you can. Watching a user follow a tutorial, you may often be amazed to see how often they choose to repeat a step. They are doing it just to see that the same thing really does happen again.
  旧 | 在你的教程中，尽量使特定步骤和结果能够被重复。这颇具挑战，例如在处理不可逆的操作时（难以返回到之前的步骤）——但请尽一切可能去寻找重复的机会。观察用户跟随教程时，你往往会惊讶地发现他们选择重复某一步骤的频率之高。他们这样做仅仅是为了亲眼确认同样的事情确实会再次发生。
  新 | 在你的教程里，尽量让某一步骤及其结果能够被重复。这有时并不容易，比如在不可逆的操作中（很难退回上一步）——但只要找得到机会，就去找。看着用户跟着教程做，你常会惊讶地发现，他们选择重复某一步的频率有多高。他们这么做，只是想亲眼看到同一件事真的又发生了一次。

  ── [tutorials]
  EN | Ruthlessly minimise explanation
  旧 | 无情地精简解释说明
  新 | 毫不留情地精简解释

  ── [tutorials]
  EN | *A tutorial is not the place for explanation.* In a tutorial, the user is focused on correctly following your directions and getting the expected results. *Later*, when they are ready, they will seek explanation, but right now they are concerned with *doing*. Explanation distracts their attention from that, and blocks their learning.
  旧 | *教程不是进行解释说明的场合。* 在教程中，用户正专注于正确遵循你的指示并获得预期结果。 **稍后**，当他们做好准备时，他们会主动寻求解释说明，但此刻他们关注的是 **行动**。解释说明会分散他们的注意力，阻碍其学习。
  新 | *教程不是做解释说明的地方*。在教程里，用户正专注于正确跟从你的指示、拿到预期的结果。*稍后*，等他们准备好了，自会去寻求解释说明；但此刻，他们在意的是*做*。解释说明会把他们的注意力从这件事上引开，阻碍他们学习。

  ── [tutorials]
  EN | For example, it's quite enough to say something like: *We're using HTTPS because it's more secure.* There is a place for extended discussion and explanation of HTTPS, but not now. Instead, provide a link or reference to that explanation, so that it's available, but doesn't get in the way.
  旧 | 例如，这样说就足够了： *我们使用 HTTPS，因为它更安全可靠。* 有关 HTTPS 的深入讨论和解释有它的位置，但不在这里。取而代之的是，提供指向该解释的链接或参考资料，以便其可用，却不会造成干扰。
  新 | 比如，这样说就足够了：*我们用 HTTPS，因为它更安全*。关于 HTTPS 的长篇讨论和解释自有它的去处，但不是现在。改为提供一条链接或参考指向那段解释，让它随手可取，又不挡路。

  ── [tutorials]
  EN | Explanation is only pertinent at the moment the *user* wants it. It is not for the documentation author to decide.
  旧 | 解释只在 *用户* 需要的时刻才相关，而非由文档作者决定。
  新 | 解释，只在*用户*想要它的那一刻才切题。这不是文档作者该决定的事。

  ── [tutorials]
  EN | Explanation is one of the hardest temptations for a teacher to resist; even experienced teachers find it difficult to accept that their students' learning does not depend on explanation. This is perfectly natural. Once we have grasped something, we rely on the power of abstraction to frame it to ourselves - and that's how we want to frame it to others. Understanding means grasping general ideas, and abstraction is the logical form of understanding - but these are not what we need in a tutorial, and it's not how successful learning or teaching works.
  旧 | 解释是教师最难抗拒的诱惑之一；即使是有经验的教师也发现难以接受学生的学习并不依赖于解释这一事实。这完全合乎情理。一旦我们理解了某事，我们就依靠抽象的力量来在内心构建它——这也是我们希望向他人呈现的方式。理解意味着把握一般概念，而抽象则是理解的逻辑形式——但这并非教程所需，也不是成功的学习或教学运作方式。
  新 | 解释是教师最难抗拒的诱惑之一；即便是经验丰富的教师，也难以接受学生的学习并不依赖解释。这再自然不过。一旦我们弄懂了什么，就会借助抽象的力量在心里把它框定成形——而我们想展示给别人的，也正是这个样子。理解意味着把握一般的观念，抽象则是理解的逻辑形式——但这些并不是教程里需要的东西，成功的学习或教学也不靠这个。

  ── [tutorials]
  EN | One must see it for oneself, to see the focused attention of a student dissolve into air, when a teacher's well-intentioned explanation breaks the magic spell of learning.
  旧 | 这需要亲眼去看：当教师好心的讲解打破了学习的魔力时，学生原本专注的注意力，如何顷刻间烟消云散。
  新 | 人非得亲眼见到，才能看到学生的专注如何顷刻化为乌有——就在教师一番好意的解释打破学习的魔法之时。

  ── [tutorials]
  EN | ... and focus on the concrete
  旧 | ...并聚焦于具体事物
  新 | ……并聚焦于具体

  ── [tutorials]
  EN | In a learning situation, your student is in the moment, a moment composed of concrete things. You are responsible for setting up and maintaining the student's flow, from one concrete action and result to another.
  旧 | 在学习情境中，学生身处由具体事物构成的当下。你负责建立并维持学生的流畅感，引导其从一个具体行动和结果走向下一个。
  新 | 在学习情境中，你的学生身处当下，而当下由一件件具体事物构成。你的责任是营造并维持学生的流畅感，让他从一个具体的行动与结果，走向下一个。

  ── [tutorials]
  EN | Focus on *this* problem, *this* action, *this* result, in such a way that you lead the learner from step to concrete step.
  旧 | 聚焦于 *这个* 问题、 *这个* 行动、 *这个* 结果，以这种方式引导学生从一步迈向具体的下一步。
  新 | *这个问题*、*这个行动*、*这个结果*——聚焦于此，从而领着学习者从一个具体步骤走向下一个。

  ── [tutorials]
  EN | It might seem that by maintaining focus on the concrete and particular that you deny the student the opportunity to see or grasp the larger general patterns, but the contrary is true. The one thing our minds do spectacularly well is to perceive general patterns from concrete examples. All learning moves in one direction: from the concrete and particular, towards the general and abstract. The latter *will* emerge from the former.
  旧 | 似乎维持对具体和个别事物的专注会剥夺学生观察或把握更大一般模式的机会，但事实恰恰相反。我们的大脑擅长的一件事就是从具体例子中感知一般模式。所有学习都朝一个方向进行：从具体和个别走向一般和抽象。后者 *将* 会从前者中涌现。
  新 | 你也许会以为，一直盯住具体和个别，就剥夺了学生看到或把握更宏大的普遍模式的机会；事实恰恰相反。我们的大脑有一件事做得极其漂亮：从具体的例子中看出普遍的模式。一切学习都朝着同一个方向走：从具体、个别，通向普遍、抽象。后者*终将*从前者之中生长出来。

  ── [tutorials]
  EN | Ignore options and alternatives
  旧 | 忽略选项和替代方案
  新 | 忽略选项与替代方案

  ── [tutorials]
  EN | Your job is to guide the learner to a successful conclusion. There may be many interesting diversions along the way (different options for the command you're using, different ways to use the API, different approaches to the task you're describing) - ignore them. *Your guidance needs to remain focused on what's required to reach the conclusion*, and everything else can be left for another time.
  旧 | 你的工作是引导学习者走向成功的结局。途中可能会有许多有趣的岔路（例如：你使用的命令的不同选项、使用 API 的不同方式、完成你所描述任务的不同方法）——请忽略它们。 *你的指导需要始终聚焦于达成所需结果所必需的内容*，其余所有东西都可以留待以后处理。
  新 | 你的职责，是把学习者一路引向成功的结局。一路上可能有许多有趣的岔路（你在用的命令还有别的选项，使用 API 还有别的路子，你要讲的任务还有别的做法）——忽略它们。*你的指引必须始终聚焦在抵达终点所必需的东西上*，其余一切都可以留到以后。

  ── [tutorials]
  EN | Doing this helps keep your tutorial shorter and crisper, and saves both you and the reader from having to do extra cognitive work.
  旧 | 这样做有助于让你的教程更简短、更精炼，同时也能为你和读者省去额外的认知工作量。
  新 | 这样做能让你的教程更简短、更利落，也省得你和读者多做额外的脑力活。

  ── [tutorials]
  EN | Aspire to perfect reliability
  旧 | 力求实现完美可靠性
  新 | 追求完美的可靠性

  ── [tutorials]
  EN | All of the above are general principles of pedagogy, but there is a special burden on the creator of a tutorial.
  旧 | 上述所有都是教育的一般原则，但教程的创作者负有特殊责任。
  新 | 以上都是教学的一般原则，但教程的创作者还背着一副特别的担子。

  ── [tutorials]
  EN | A tutorial must inspire confidence. Confidence can only be built up layer by layer, and is easily shaken. At every stage, when you ask your student to do something, they must see the result you promise. A learner who follows your directions and doesn't get the expected results will quickly lose confidence, in the tutorial, the tutor and themselves.
  旧 | 教程必须能激发信心。信心只能层层累积，且极易动摇。在每个阶段，当你要求学生执行某项操作时，他们必须看到你所承诺的结果。如果学习者遵循你的指示却未获得预期结果，他们会迅速失去对教程、导师乃至自身的信心。
  新 | 教程必须能让人生出信心。信心只能一层一层垒起来，却极易动摇。每一个阶段，你让学生做什么，他们都必须看到你许诺的结果。学习者照着你的指示做，却没拿到预期的结果，很快就会失去信心——对教程、对导师、也对自己。

  ── [tutorials]
  EN | You are required to be present, but condemned to be absent.
  旧 | 你被要求在场，却又注定缺席。
  新 | 要求你在场，却注定缺席。

  ── [tutorials]
  EN | A teacher who's there with the learner can rescue them when things go wrong. In a tutorial, you can't do that. Your tutorial ought to be so well constructed that things *can't* go wrong, that your tutorial works for every user, every time.
  旧 | 一位与学习者同在的教师可以在事情出错时救他们于危难之中。而在教程中，你却做不到这一点。你的教程应当构造得如此精良，以至于事情 *不可能* 出错；它应能每次都对每一位用户有效运作。
  新 | 教师陪在学习者身边，出了岔子还能救一把。在教程里，你做不到。你的教程应当构造得如此严密：事情*不可能*出错，对每一位用户、每一次，它都管用。

  ── [tutorials]
  EN | It's hard work to create a reliable experience, but that is what you must aspire to in creating a tutorial.
  旧 | 创建一个可靠的用户体验是一项艰巨的工作，但在编写教程时，这正是你必须追求的目标。
  新 | 打造一份可靠的体验是件苦功夫，但编写教程时，这正是你必须追求的目标。

  ── [tutorials]
  EN | Your tutorial will have flaws and gaps, however carefully it is written. You won't discover them all by yourself, you will have to rely on users to discover them for you. The only way to learn what they are is by finding out what actually happens when users do the tutorial, through extensive testing and observation.
  旧 | 无论你的教程写得多么仔细，它总会存在缺陷和漏洞。你无法独自发现所有这些问题，必须依靠用户来帮你发现。唯一能了解这些问题的方法，是通过广泛的测试和观察，找出当用户实际操作教程时真正发生的事情。
  新 | 无论教程写得多仔细，总会有缺陷和漏洞。你没法一个人把它们全找出来，只能靠用户替你发现。想知道它们是什么，唯一的办法是通过大量的测试和观察，弄清用户真的照着教程做时会发生什么。

  ── [tutorials]
  EN | The first-person plural affirms the relationship between tutor and learner: you are not alone; we are in this together.
  旧 | 第一人称复数强调了导师与学习者之间的关系：你并不孤单，我们要共同努力。
  新 | 第一人称复数确认了导师与学习者之间的关系：你并不孤单；这件事我们一起做。

  ── [tutorials]
  EN | Describe what the learner will accomplish.
  旧 | 描述学习者将要完成的任务。
  新 | 说明学习者将达成什么。

  ── [tutorials]
  EN | First, do x. Now, do y. Now that you have done y, do z.
  旧 | 首先，执行 x。现在，执行 y。既然你已经完成了 y，接下来执行 z。
  新 | 先做 x。现在做 y。既然做完了 y，就做 z。

  ── [tutorials]
  EN | No room for ambiguity or doubt.
  旧 | 不容许任何含糊或怀疑。
  新 | 不留一丝含糊或怀疑的余地。

  ── [tutorials]
  EN | We must always do x before we do y because... (see Explanation for more details).
  旧 | 我们必须始终先做 x，再做 y，因为……（更多细节见“解释说明”）。
  新 | 我们必须先做 x 再做 y，因为……（详见“解释说明”）。

  ── [tutorials]
  EN | Provide minimal explanation of actions in the most basic language possible. Link to more detailed explanation.
  旧 | 用最基本的语言提供行动的最小化解释说明。链接至更详细的解释说明。
  新 | 用最基础的语言，对行动做最低限度的解释说明。链接到更详细的解释说明。

  ── [tutorials]
  EN | The output should look something like ...
  旧 | 输出应大致如下所示...
  新 | 输出应该大致像这样……

  ── [tutorials]
  EN | Give your learner clear expectations.
  旧 | 给予你的学习者明确的期望。
  新 | 给学习者明确的预期。

  ── [tutorials]
  EN | Notice that ... Remember that ... Let's check ...
  旧 | 注意...请记住...让我们检查...
  新 | 注意……记住……我们来检查一下……

  ── [tutorials]
  EN | Give your learner plenty of clues to help confirm they are on the right track and orient themselves.
  旧 | 为你的学习者提供充分的提示，以帮助确认他们处于正确的方向并确定自身的方位。
  新 | 给学习者足够多的线索，帮他们确认自己走对了路，也帮他们找准方位。

  ── [tutorials]
  EN | Describe (and admire, in a mild way) what your learner has accomplished.
  旧 | 描述（并以温和的方式赞赏）你的学习者的成就。
  新 | 描述（并温和地赞赏）学习者取得的成就。

  ── [tutorials]
  EN | A child proudly showing a dish he has helped prepare
  旧 | 一个孩子自豪地展示他帮忙准备的菜肴
  新 | 一个孩子自豪地展示他帮忙做好的菜

  ── [tutorials]
  EN | Someone who has had the experience of teaching a child to cook will understand what matters in a tutorial, and just as importantly, the things that don't matter at all.
  旧 | 曾有过教孩子做饭经验的人，会明白在教程中什么才是重要的，同样重要的是，哪些完全不重要。
  新 | 教过孩子做饭的人，会明白教程里什么要紧；同样重要的是，也明白什么根本不要紧。

  ── [tutorials]
  EN | It really doesn't matter what the child makes, or how correctly they do it. The value of a lesson lies in what the child gains, not what they produce.
  旧 | 孩子做什么并不真正重要，也不在于他们做得是否正确。课程的价值在于孩子获得的收获，而非他们产出的东西。
  新 | 孩子做出什么，做得对不对，其实都无所谓。一堂课的价值，在于孩子得到了什么，而不在于他做出了什么。

  ── [tutorials]
  EN | Success in a cooking lesson with a child is not the culinary outcome, or whether the child can now repeat the processes on their own. Success is when the child acquires the knowledge and skills you were hoping to impart.
  旧 | 与孩子一起上烹饪课的成功，不在于最终的美食成果，也不在于孩子是否现在能独立重复这些流程。成功在于孩子习得了你希望传授的知识和技能。
  新 | 跟孩子上烹饪课，成功不在于最后做出什么菜，也不在于孩子从此能不能自己重复那些流程。成功，是孩子真的学到了你希望传授的知识和技能。

  ── [tutorials]
  EN | It's a crucial condition of this that the child discovers pleasure in the experience of being in the kitchen with you, and wants to return to it. Learning a skill is never a once and for all matter. Repetition is always required.
  旧 | 其中一个关键条件是：孩子必须从与你一起在厨房里的经历中发现乐趣，并希望再次回到那里。掌握一项技能从来不是"一劳永逸"的事。重复总是必要的。
  新 | 这里的一个关键条件是：孩子要从和你一起待在厨房里的经历中发现乐趣，并且愿意再回来。学一门技能，从来不是“一劳永逸”的事。重复永远少不了。

  ── [tutorials]
  EN | Meanwhile, the cooking lesson might be framed around the idea of learning how to prepare a particular dish, but what we actually need the child to learn might be things like: *that we wash our hands before handling food*; *how to hold a knife*; *why the oil must be hot*; *what this utensil is called*, *how to time and measure things*.
  旧 | 与此同时，烹饪课可以围绕学习制作特定菜肴这一想法来构建框架，但我们实际上需要孩子学习的可能是诸如： *我们在处理食物前要洗手*； *如何握刀*； *为什么油必须加热*； *这个器具叫什么*； *如何定时和测量* 等内容。
  新 | 与此同时，烹饪课或许是围绕“学做某道菜”来搭框架的，但我们真正需要孩子学的，可能是这些：*碰食物之前要先洗手*；*怎么握刀*；*为什么油一定要热*；*这件器具叫什么*，*怎么把握时间和分量*。

  ── [tutorials]
  EN | The child learns all this by working alongside you in the kitchen; in its own time, at its own pace, **through the activities** you do together, and not from the things you say or show.
  旧 | 孩子通过与你在厨房并肩工作，学到这一切：在你们共同进行的 **活动** 当中，按照它自己的时机和节奏，而不是靠你说的话或展示的东西。
  新 | 孩子是在厨房里和你并肩干活时学会这一切的：按他自己的时间、自己的节奏，**通过你们一起做的活动**，而不是靠你说的话或展示的东西。

  ── [tutorials]
  EN | With a young child, you will often find that the lesson suddenly has to end before you'd completed what you set out to do. This is normal and expected; children have short attention spans. But as long as the child managed to achieve something - however small - and enjoyed doing it, it will have laid down something in the construction of its technical expertise, that can be returned to and built upon next time.
  旧 | 和年幼的孩子一起学习时，课程常会在原定目标尚未完成前突然结束。这很正常，也在预料之中；孩子的注意力持续时间较短。但只要孩子完成了某件事——无论多小——并从中获得乐趣，就已为其技艺能力打下一块基础，下次可以回到这里继续构建。
  新 | 跟年幼的孩子在一起，你常会发现，还没做完原打算做的事，课就不得不突然结束了。这很正常，也在意料之中；孩子的注意力本来就短。但只要孩子做成了点什么——无论多小——而且做得开心，他就为自己的技术能力添上了一块砖，下次可以回到这里继续往上垒。
tutorials-how-to          71 条  改动  65

  ── [tutorials-how-to]
  EN | In Diátaxis, tutorials and how-to guides are strongly distinguished. It’s a distinction that’s often not made; in fact the single most common conflation made in software product documentation is that between the *tutorial* and the *how-to guide*.
  旧 | 在 Diátaxis 中，教程和实践指南有着严格的区别。这是一种常常被忽略的区分；事实上，软件产品文档中最常见的混淆，就是把 *教程* 和 *实践指南* 混为一谈。
  新 | 在 Diátaxis 中，教程与实践指南被严格区分开来。可这种区分常常无人做出；事实上，软件产品文档里最常见的一种混淆，就是把*教程*和*实践指南*混为一谈。

  ── [tutorials-how-to]
  EN | So: what *is* the difference between tutorials and how to-guides? Why does it matter? And why do they get confused?
  旧 | 那么：教程与实践指南之间到底有什么区别？这为什么重要？它们为什么会被人混淆？
  新 | 那么：教程与实践指南之间*到底*有什么区别？这件事为什么重要？它们又为什么会被混淆？

  ── [tutorials-how-to]
  EN | These are all good questions. Let’s start with the last one. *If the distinction is really so important, why isn’t it more obvious?*
  旧 | 这些都是很好的问题。让我们从最后一个问题开始。 *如果这种区别真的如此重要，为什么它不那么显而易见？*
  新 | 这些都是很好的问题。我们先从最后一个说起。*如果这个区别真的这么重要，为什么它不那么显而易见？*

  ── [tutorials-how-to]
  EN | In important respects, tutorials and how-to guides are indeed similar. They are both practical guides: they contain directions for the user to follow. They’re not there to explain or convey information. They exist to guide the user in what to *do* rather than what there is *to know or understand*.
  旧 | 在许多重要方面，教程和实践指南确实相似。它们都是实用指南：包含用户需遵循的指引。它们的存在，是为了引导用户 *该做什么*，而不是该 *知道或理解什么*。
  新 | 在许多重要方面，教程和实践指南确实相似。两者都是实用指南：里面给出供用户遵循的指引。它们的存在，不是为了解释或传达信息，而是要引导用户：该*做什么*，而不是该*知道或理解什么*。

  ── [tutorials-how-to]
  EN | They both set out steps for the reader to follow, and they both promise that if the reader follows those steps, they’ll arrive at a successful conclusion. Neither of them make much sense except for the user who has their hands on the machinery, ready to do things. They both describe ordered sequences of actions. You can’t expect success unless you perform the actions in the right order.
  旧 | 两者都为读者设定了需遵循的步骤，并承诺若按此执行即可达成成功的结论。对没有亲手操作设备、准备动手的用户来说，两者都没什么意义。它们都描述了有序的行动序列。若不按正确顺序执行这些行动，便无法获得成功。
  新 | 两者都为读者列出要遵循的步骤，也都承诺：只要读者照着做，就会抵达一个成功的结果。除非用户已经把手搭在系统上、随时准备动手，否则两者都意义不大。它们描述的都是有序的行动序列。除非你按正确的顺序执行这些行动，否则别指望成功。

  ── [tutorials-how-to]
  EN | Diátaxis insists that what matters in documentation is the needs of the user, and it's by paying attention to this that we can correctly distinguish between tutorials and how-to guides.
  旧 | Diátaxis 坚持认为，文档中重要的是用户需求，只有关注这一点，我们才能正确区分 **教程** 和 **实践指南**。
  新 | Diátaxis 坚持认为，文档中重要的是用户的需求；正是靠关注这一点，我们才能正确区分教程与实践指南。

  ── [tutorials-how-to]
  EN | Sometimes the user is **at study**, and sometimes the user is **at work**. Documentation has to serve both those needs.
  旧 | 有时用户处于 **学习** 状态，有时用户处于 **工作** 状态。文档必须同时满足这两方面的需求。
  新 | 有时用户处于**学（习得）**的状态，有时用户处于**用（应用）**的状态。文档必须同时满足这两种需求。

  ── [tutorials-how-to]
  EN | A tutorial serves the needs of the user who is at study. Its obligation is *to provide a successful learning experience*. A how-to guide serves the needs of the user who is at work. Its obligation is *to help the user accomplish a task*. These are completely different needs and obligations, and they are why the distinction between tutorials and how-to guides matters: tutorials are **learning-oriented**, and how-to guides are **task-oriented**.
  旧 | **教程** 服务于处于 **学习** 状态的用户。它的义务是 *提供成功的学习体验*。 **实践指南** 服务于处于 **工作** 状态的用户。它的义务是 *帮助用户完成任务*。这些是完全不同的需求和义务，也是区分 **教程** 和 **实践指南** 的重要性所在： **教程** 是 **以学习为导向** 的，而 **实践指南** 是 **以任务为导向** 的。
  新 | 教程服务于处于学习状态的用户。它的义务是*提供一次成功的学习体验*。实践指南服务于处于工作状态的用户。它的义务是*帮助用户完成一项任务*。这些需求和义务截然不同，而教程与实践指南之所以必须区分，原因正在于此：教程**面向学习**，实践指南**面向任务**。

  ── [tutorials-how-to]
  EN | At study and at work
  旧 | 学习与工作
  新 | 学与用

  ── [tutorials-how-to]
  EN | We can consider this from the perspective of an actual example. Let’s say you’re in medicine: a doctor, someone who needs to acquire and apply the practical, clinical skills of their craft.
  旧 | 我们可以从一个实际例子来考虑这个问题。假设你从事医学工作：一名医生，需要 **习得** 并 **应用** 其 **技艺** 的实用临床技能。
  新 | 我们不妨用一个实际的例子来看。假设你身在医学这一行：一名医生，需要习得并应用自己技艺里的那些实用临床技能。

  ── [tutorials-how-to]
  EN | As a doctor, sometimes you will be in work situations, *applying your skills*, and sometimes you will be in study situations, *acquiring skills* (all good doctors, even those with long careers behind them, continue to study to improve their skills).
  旧 | 作为医生，有时你会处于工作状态， *应用你的技能*，有时你会处于学习状态， *习得技能* （所有优秀的医生，即便是那些有着漫长职业生涯的人，也会继续学习以提高技能）。
  新 | 作为医生，有时你身处工作情境，*应用*自己的技能；有时你身处学习情境，*习得*技能（所有好医生，哪怕已经从业多年，也仍在继续学习，以精进自己的技能）。

  ── [tutorials-how-to]
  EN | At study
  旧 | 在学习中
  新 | 学（习得）

  ── [tutorials-how-to]
  EN | Early on in your training, you’ll learn how to suture a wound. You’ll start in the lab with your fellow students, at benches with small skin pads in front of you (skin pads are blocks of synthetic material in various layers that represent the epidermis, fat and other tissues. They have a similar hardness and texture to human flesh, and behave somewhat similarly when they’re cut and stitched). You’ll be provided with exactly what you need - gloves, scalpel, needle, thread and so on - and step-by-step you’ll be shown what to do, and what will happen when you do it.
  旧 | 在训练初期，你将学会缝合伤口。你将与同学一起在实验室开始练习，面前是放置有小型皮肤垫的台座（皮肤垫是由多层合成材料制成的块状物，代表表皮、脂肪和其他组织。它们的硬度和纹理与人体肌肤相似，在被切割和缝合时的表现也颇为接近）。你将获得所需的一切——手套、手术刀、针线等——并一步步地接受指导，了解该做什么以及这样做会产生什么结果。
  新 | 训练刚开始，你会学着缝合伤口。你和同学一起走进实验室，坐在实验台前，面前摆着小块皮肤垫（皮肤垫是用合成材料做成的多层块状物，代表表皮、脂肪和其他组织，硬度和质感接近人的皮肉，切开和缝合时的表现也有几分相似）。需要的东西会一一备齐——手套、手术刀、针、线等等——然后有人一步步演示该做什么，以及这么做会发生什么。

  ── [tutorials-how-to]
  EN | And then it’s your turn. You will pick up the scalpel and tentatively draw it across the top of the pad, and make an ineffectual incision into the top layer (maybe a teaching assistant will tease you, asking what this poor pad has done, that it deserves such a nasty scratch). Your neighbour will look dismayed at their own attempt, a ragged cut of wildly uneven depths that looks like something from a knife-fight.
  旧 | 然后轮到你了。你将拿起手术刀，试探性地将其在垫子顶端划动，并对顶层造成一道无效切口（也许教学助教会取笑你，问道：这可怜的小垫子究竟做了什么，值得遭受如此粗暴的划痕）。你的邻居则对自己那次的尝试感到沮丧——一道参差不齐、深浅不一的乱切口，像是持刀斗殴留下的伤。
  新 | 然后轮到你了。你拿起手术刀，试探着在垫子表面划一下，在表层留下一道不痛不痒的切口（也许助教会取笑你：这可怜的小垫子做了什么，要挨这么难看的一划？）。旁边的同学看着自己的手笔一脸沮丧——一道毛糙的切口，深浅悬殊，活像刀斗留下的伤。

  ── [tutorials-how-to]
  EN | After a few attempts, with feedback and correction from the tutor, you’ll have made a more or less clean cut that mostly goes through the fat layer without cutting into the muscle beneath. Triumph!
  旧 | 经过几次尝试，并在导师的反馈与纠正后，你将能够切割出一条相对平整的切口，主要穿过脂肪层而不会伤及下方的肌肉。大功告成！
  新 | 试了几次，再加上导师的反馈与纠正，你终于划出一道还算平整的切口，基本穿过脂肪层，没有切到下面的肌肉。胜利！

  ── [tutorials-how-to]
  EN | But now you’re being asked to stitch it back up again! You’ll watch the tutor demonstrate deftly and precisely, closing the wound in the pad with a few neat, even stitches. You, on the other hand, will fumble with the thread. You will hold things in the wrong hand and the wrong way round and put them down in the wrong places. You will drop the needle. The thread will fall out. You will be told off for failing to maintain sterility.
  旧 | 但如今你被要求再次将伤口缝合起来！你将观看导师灵巧而精准地演示，仅用几针均匀整齐的缝线便将垫子上的伤口闭合。而你，另一方面，则会笨手笨脚地与线团纠缠不清。你将用错手、拿反物件，并将它们随意放置在不该放的地方。你会掉针，线也会从针眼里滑落。你还会因未能维持无菌状态而受到斥责。
  新 | 可现在，又要你把它缝回去！你看导师演示得又灵巧又精准，几针干净利落的缝线就把垫子上的伤口合上了。轮到你，却只能跟那根线较劲。哪只手拿、哪头朝上，你全弄反，东西也放得不是地方。你会掉针，线会脱出来。你会因为没保持无菌而挨训。

  ── [tutorials-how-to]
  EN | Eventually, you’ll actually get to stitch the wound. You will puncture the skin in the wrong places and tear the edges of the cut. Your final result will be an ugly scene of stretched and puckered skin and crude, untidy stitches. The teaching assistants will have some critical things to say even about parts of it that you thought you’d got right.
  旧 | 最终，你终于真正开始缝合伤口了。你会将刺入皮肤的位置弄错，扯裂切口边缘。你的最终结果将是一片令人难堪的景象：被拉伸和起皱的皮肤以及粗制滥造、杂乱无章的缝线。即使对于那些你自以为做得正确的部分，教学助教也会提出一些严厉的批评。
  新 | 终于，你真的动手缝伤口了。下针的位置处处不对，切口边缘也被你扯破。最后的成果是一片惨状：皮肤绷着、皱着，缝线又粗又乱。就连你自以为缝对了的地方，助教们也有一番批评要说。

  ── [tutorials-how-to]
  EN | But, *you will have stitched your first wound*. And you will come back to this lesson again and again, and bit by bit your fumbling will turn into confident practice. You will have acquired basic competence. You will have **learned by doing**.
  旧 | 但是， *你将缝合了自己的第一道伤口*。你将一次又一次地回到这一课，一点一点地将笨拙的操作转化为自信的实践。你将具备基本的能力。你 **通过动手而学会了**。
  新 | 但是，*你已经缝完了自己的第一道伤口*。你会一次又一次回到这一课，笨拙会一点一点变成自信的实践。你会获得基本的能力。你**在动手中学会了**。

  ── [tutorials-how-to]
  EN | This is a tutorial. It’s a *lesson*, safely in the hands of an instructor, a teacher who looks after the interests of a pupil.
  旧 | 这是一个教程。它是一堂 *课程*，在导师的掌控之中——这位教师会照顾到学员的利益。
  新 | 这是一个教程。它是一堂*课*，安全地交在讲师手中——一位照看学生利益的教师。

  ── [tutorials-how-to]
  EN | At work
  旧 | 在工作中
  新 | 用（应用）

  ── [tutorials-how-to]
  EN | Now, let’s think about the doctor at work. As a doctor at work, you are already competent. You have learned and refined clinical skills such as suturing, as well as many others, and you’re able to put them together on a daily basis to apply them to medical situations in the real world.
  旧 | 现在，让我们思考一下工作中的医生。作为一名在职医生，你已经是合格的。你已经学习并磨练了缝合等临床技能，还有许多其他技能，并且能够每天将它们结合起来，应用于现实世界中的医疗情况。
  新 | 现在，想想工作中的医生。作为一名工作中的医生，你早已具备能力。你学习并磨练过缝合这类临床技能，也学会了许多别的技能，每天都能把它们组合起来，应用到现实世界里的各种医疗情境。

  ── [tutorials-how-to]
  EN | Consider a standard appendectomy. A clinical manual will list the equipment and personnel required in the theatre. It will show how to station the members of the team, and how to lay out the required tools, stands and monitors. It will proceed step-by-step through the actions the team will need to follow, ending with the formal handover to the post-operative team.
  旧 | 考虑一次标准的阑尾切除术。临床手册将列出手术室所需的设备和人员。它将展示如何安排团队成员的站位，以及如何布置所需的工具、支架和显示器。它将按步骤依次介绍团队需要遵循的行动，最后以正式交接给术后团队告终。
  新 | 以一台标准的阑尾切除术为例。临床手册会列出手术室所需的设备和人员，说明团队成员各自站在哪里，所需的器械、支架和监护仪怎么摆放；然后一步步走完团队需要执行的那些行动，最后以正式交接给术后团队收尾。

  ── [tutorials-how-to]
  EN | The manual will show what incisions need to be made where, but they will depend on whether you’re performing an open or a laparoscopic procedure, whether you have pre-operative imaging to rely on or not, and so on. It will include special steps or checks to be made in the case of an infant or juvenile patient, or when converting to an open appendectomy mid-procedure. Many of the steps will be of the form *if this, then that*.
  旧 | 手册将说明在何处需要做何种切口，但这取决于你进行的是开放手术还是腹腔镜手术，是否依赖术前影像等。它将包括针对婴儿或青少年患者，或在手术过程中转为开放阑尾切除术等情况下的特殊步骤或检查。许多步骤的形式是 *如果这个，那么那个*。
  新 | 手册会说明该在哪里下什么切口，但切口取决于你做的是开放手术还是腹腔镜手术、有没有术前影像可供参考，等等。如果患者是婴儿或青少年，或者手术中途要转为开放阑尾切除术，手册里也会列出专门的步骤或核对项。许多步骤都是*如果这样，那就那样*的形式。

  ── [tutorials-how-to]
  EN | Having a manual helps ensure that all the steps are done in the right order and none are omitted. As a team, you’ll check through details of a procedure to remind yourselves of key steps; sometimes you'll refer to it during the procedure itself.
  旧 | 拥有手册有助于确保所有步骤按正确顺序完成且无一遗漏。作为团队，你们将审查程序的细节以提醒自己关键步骤；有时你甚至会在进行手术本身时查阅它。
  新 | 有手册在手，就有助于确保所有步骤都按正确顺序完成，一个也不漏。作为团队，你们会一起过一遍操作的细节，提醒彼此关键的步骤；有时手术做到一半，还会翻开来看。

  ── [tutorials-how-to]
  EN | Even for routine surgical operations, clinical manuals contain lists of steps and checks. These manuals are how-to guides. They are not there to teach you - you already have your skills. You already know these processes. They are there to guide you safely in your clinical practice to accomplish a particular task - **they serve your work**.
  旧 | 即使是常规外科手术，临床手册也包含步骤和检查清单。这些手册是实践指南。它们并非为了教你——你已经具备这些技能。你已经了解这些流程。它们旨在引导你在临床实践中安全地完成特定任务—— **它们服务于你的工作**。
  新 | 即便是常规外科手术，临床手册里也有步骤清单和核对清单。这些手册就是实践指南。它们不是用来教你的——你已经有技能了，这些流程你早就知道。它们的作用，是在你的临床实践中安全地引导你完成某一项具体任务——**它们服务于你的工作**。

  ── [tutorials-how-to]
  EN | Understanding the distinction
  旧 | 理解区别
  新 | 理解这一区别

  ── [tutorials-how-to]
  EN | The distinction between a lesson in medical school and a clinical manual is the distinction between a tutorial and a how-to guide.
  旧 | 医学院中的一课与临床手册之间的区别，在于教程与实践指南之间的区别。
  新 | 医学院里的一堂课与临床手册之间的区别，就是教程与实践指南之间的区别。

  ── [tutorials-how-to]
  EN | A tutorial’s purpose is **to help the pupil acquire basic competence**.
  旧 | 教程的目的是 **帮助学生习得基本能力**。
  新 | 教程的目的，是**帮助学生习得基本能力**。

  ── [tutorials-how-to]
  EN | A how-to guide’s purpose is **to help the already-competent user perform a particular task correctly**.
  旧 | 实践指南的目的是 **帮助已经具备能力的用户正确执行特定任务**。
  新 | 实践指南的目的，是**帮助已经具备能力的用户正确完成某一项具体任务**。

  ── [tutorials-how-to]
  EN | A tutorial **provides a learning experience**. People learn skills through practical, hands-on experience. What matters in a tutorial is what the learner *does*, and what they experience while doing it.
  旧 | 教程 **提供学习体验**。人们通过实际动手经验习得技能。在教程中重要的是学习者 *做了什么* 以及他们在做这件事时所获得的体验。
  新 | 教程**提供一次学习体验**。人是在实际动手的体验中学会技能的。教程里要紧的，是学习者*做了什么*，以及在做的时候感受到了什么。

  ── [tutorials-how-to]
  EN | A how-to guide **directs the user’s work**.
  旧 | 实践指南 **引导用户的工作**。
  新 | 实践指南**引导用户的工作**。

  ── [tutorials-how-to]
  EN | The tutorial follows a **carefully-managed path**, starting at a given point and working to a conclusion. Along that path, the learner must have the *encounters* that the lesson requires.
  旧 | 教程遵循一条 **精心管理的路径**，从给定的起点开始工作直至得出结论。沿着这条路径，学习者必须获得课程所要求的那些 *相遇*。
  新 | 教程走的是一条**精心管理的路径**，从既定的起点出发，一路走到结论。沿着这条路径，学习者必须经历课程所要求的那些*相遇*。

  ── [tutorials-how-to]
  EN | The how-to guide aims for a successful *result*, and guides the user along the safest, surest way to the goal, but **the path can’t be managed**: it’s the real world, and anything could appear to disrupt the journey.
  旧 | 实践指南旨在实现成功的 *结果*，并引导用户通过最安全、最可靠的方式到达目标，但 **路径无法被管理**：这是现实世界，任何事情都可能出现来扰乱旅程。
  新 | 实践指南求的是一个成功的*结果*，引导用户沿着最安全、最稳妥的路走向目标，但**路径无法管理**：这是现实世界，什么都可能冒出来打断行程。

  ── [tutorials-how-to]
  EN | A tutorial **familiarises the learner** with the work: with the tools, the language, the processes and the way that what they’re working with behaves and responds, and so on. Its job is to introduce them, manufacturing a structured, repeatable encounter with them.
  旧 | 教程让学习者 *熟悉* 工作：包括工具、语言、流程，以及他们所操作对象的行为和响应方式等等。它的职责是引介这些东西，营造出有结构、可重复的相遇。
  新 | 教程**让学习者熟悉**这项工作：熟悉工具、语言、流程，熟悉他所打交道的对象怎么表现、怎么回应，等等。它的职责就是把这些引介给他，营造出一种有结构、可重复的相遇。

  ── [tutorials-how-to]
  EN | The how-to guide can and should **assume familiarity** with them all.
  旧 | 实践指南可以且应当 **假定对其全部熟悉**。
  新 | 实践指南可以，也应当**假定读者对这一切都已熟悉**。

  ── [tutorials-how-to]
  EN | The tutorial takes place in a **contrived setting**, a learning environment where as much as possible is set out in advance to ensure a successful experience.
  旧 | 教程发生在一种 **人为搭建的场景** 中，即一个事先尽可能安排妥当、以确保体验成功的学习环境。
  新 | 教程发生在**人为搭建的场景**里：一个尽可能事先安排停当、以确保体验成功的学习环境。

  ── [tutorials-how-to]
  EN | A how-to guide applies to the **real world**, where you have to deal with what it throws at you.
  旧 | 实践指南适用于 **真实世界**，在那里你必须应对它向你抛出的任何挑战。
  新 | 实践指南面向**真实世界**，在那里，你得应付它扔过来的一切。

  ── [tutorials-how-to]
  EN | The tutorial **eliminates the unexpected**.
  旧 | 教程 **消除不可预见性**。
  新 | 教程**消除意外**。

  ── [tutorials-how-to]
  EN | The how-to guide must **prepare for the unexpected**, alerting the user to its possibility and providing guidance on how to deal with it.
  旧 | 实践指南必须 **为不可预见性做准备**，提醒用户其可能性，并提供如何应对的指导。
  新 | 实践指南必须**为意外做准备**，提醒用户它有可能出现，并给出应对的指引。

  ── [tutorials-how-to]
  EN | A tutorial’s path follows a single line. **It doesn’t offer choices or alternatives**.
  旧 | 教程的路径遵循单一线索。 **它不提供选择或替代方案**。
  新 | 教程的路径是一条单线。**它不提供选择，也不提供替代方案**。

  ── [tutorials-how-to]
  EN | A **how-to guide will typically fork and branch**, describing different routes to the same destination: *If this, then that. In the case of ..., an alternative approach is to…*
  旧 | 实践指南 **通常会分叉并分支**，描述通往同一目的地的不同路线： *如果是这样，那就那样。在...的情况下，另一种方法是…*
  新 | **实践指南通常会分叉、分支**，描述通往同一个目的地的不同路线：*如果这样，那就那样。在……的情况下，另一种做法是……*

  ── [tutorials-how-to]
  EN | A tutorial **must be safe**. No harm should come to the learner; it must always be possible to go back to the beginning and start again.
  旧 | 教程 **必须安全**。学习者不应受到伤害；始终能够回到起点重新开始。
  新 | 教程**必须安全**。学习者不应受到任何伤害；任何时候都必须能够回到开头，重新来过。

  ── [tutorials-how-to]
  EN | A how-to guide **cannot promise safety**; often there’s only one chance to get it right.
  旧 | 实践指南 **无法承诺安全**；往往只有一次机会做对。
  新 | 实践指南**无法承诺安全**；常常只有一次做对的机会。

  ── [tutorials-how-to]
  EN | In a tutorial, **responsibility lies with the teacher**. If the learner gets into trouble, that's the teacher's problem to put right.
  旧 | 在教程中， **责任在于教师**。如果学习者陷入麻烦，那是教师需要解决的问题。
  新 | 在教程里，**责任在教师**。学习者要是陷入麻烦，那是教师该去解决的问题。

  ── [tutorials-how-to]
  EN | In a how-to guide, **the user has responsibility** for getting themselves in and out of trouble.
  旧 | 在实践指南中， **责任在用户**——自己惹的麻烦，自己脱身。
  新 | 在实践指南里，**责任在用户**——自己惹的麻烦，自己脱身。

  ── [tutorials-how-to]
  EN | The learner **may not even have sufficient competence to ask the questions** that a tutorial answers.
  旧 | 学习者 **甚至可能不具备足够的能力来提出教程所解答的问题**。
  新 | 学习者**甚至可能还不具备足够的能力去提出**教程所回答的那些问题。

  ── [tutorials-how-to]
  EN | A how-to guide can assume that **the user is asking the right questions in the first place**.
  旧 | 实践指南可以假定 **用户从一开始就在问正确的问题**。
  新 | 实践指南可以假定，**用户一开始就问对了问题**。

  ── [tutorials-how-to]
  EN | The tutorial is **explicit about basic things** - where to do things, where to put them, how to manipulate objects. It addresses the embodied experience - in our medical example, how hard to press, how to hold an implement; in a software tutorial, it could be where to type a command, or how long to wait for a response.
  旧 | 教程会 **明确说明基础事项** ——在哪里执行操作、放在何处、如何操控对象。它处理具身化的体验——在医疗示例中，用力按的力度有多大、如何握住器械；在软件教程中，则是应该在何处输入命令，或需要等待多久才能收到响应。
  新 | 教程**把基础的事情讲得明明白白**——在哪儿做、东西放哪儿、怎么摆弄物件。它照顾的是身体上的体验——在医学例子里，是用多大劲按、器械怎么握；在软件教程里，可能就是在哪里输入命令，或者要等多久才有响应。

  ── [tutorials-how-to]
  EN | A how-to guide relies on this as **implicit knowledge** - even bodily knowledge.
  旧 | 实践指南依赖这种作为 **隐性知识** 的内容——甚至是身体层面的知识。
  新 | 实践指南则把这一切当作**隐性知识**来依赖——甚至是身体上的知识。

  ── [tutorials-how-to]
  EN | A tutorial is **concrete and particular** in its approach. It refers to the specific, known, defined tools, materials, processes and conditions that we have carefully set before the learner.
  旧 | 教程采取 **具体且特定** 的方法。它指代那些我们已为学习者精心准备的具体、已知、明确的工具、材料、过程和条件。
  新 | 教程的做法**具体而特定**。它指的是那些具体、已知、明确的工具、材料、流程和条件——都是我们精心摆在学习者面前的东西。

  ── [tutorials-how-to]
  EN | The how-to guide has to take a **general** approach: many of these things will be unknowable in advance, or different in each real-world case.
  旧 | 实践指南必须采取 **一般化** 的方法：其中许多事物在事先无法预知，或在实际案例中各不相同。
  新 | 实践指南则只能采取**一般化**的做法：这些东西很多事先无从知晓，或者每个现实情形里都不一样。

  ── [tutorials-how-to]
  EN | The tutorial **teaches general skills and principles** that later could be applied to a multitude of cases.
  旧 | 教程 **教授通用的技能和原则**，这些后续可应用于多种情况。
  新 | 教程**教的是通用技能和原则**，日后可以应用到许许多多的情形上。

  ── [tutorials-how-to]
  EN | The user following a how-to guide is doing so in order to **complete a particular task**.
  旧 | 遵循实践指南的用户这样做是为了 **完成特定任务**。
  新 | 用户照着实践指南做，是为了**完成某一项具体任务**。

  ── [tutorials-how-to]
  EN | None of these distinctions are arbitrary. They all emerge from the distinction between **study** and **work**, which we understand as a key distinction in making sense of what the user of documentation needs.
  旧 | 这些区别并非随意划定。它们均源于 **学习** 与 **工作** 之间的区别，我们将其视为理解文档用户需求的关键区别。
  新 | 这些区别没有一处是随意划定的。它们都出自**学（习得）**与**用（应用）**之别；要弄清文档用户需要什么，我们认为这是一个关键的区别。

  ── [tutorials-how-to]
  EN | A common but understandable conflation is to see the difference between tutorials and how-to guides as being the difference between **the basic** and **the advanced**.
  旧 | 一个常见但可理解的混淆是将教程与实践指南之间的差异等同于 **基础** 与 **进阶** 之间的差异。
  新 | 一种常见但情有可原的混淆，是把教程与实践指南的区别看成**基础**与**进阶**的区别。

  ── [tutorials-how-to]
  EN | After all, tutorials are for learners, while how-to guides are for already-skilled practitioners. Tutorials must cover the basics, while how-to guides have to deal with complexities that learners should not have to face.
  旧 | 毕竟，教程面向学习者，而实践指南面向已具备技能的从业者。教程必须涵盖基础知识，而实践指南则需处理学习者不应面对的复杂问题。
  新 | 毕竟，教程是给学习者的，实践指南则是给已经具备技能的实践者的。教程必须涵盖基础，实践指南却要处理那些不该让学习者去面对的复杂问题。

  ── [tutorials-how-to]
  EN | However, there’s more to the story. Consider a clinical procedure manual: it could be a manual for a basic routine procedure, of very low complexity. It could describe steps for mundane matters such as correct completion of paperwork or disposal of particular materials. *How-to guides can, do and often should cover basic procedures.*
  旧 | 然而，事情并非如此简单。以临床操作手册为例：它可以是关于基础常规操作的手册，复杂度极低；也可以描述诸如正确填写文件或处置特定材料等日常事务的步骤。 **实践指南可以且往往应该涵盖基本操作流程**。
  新 | 然而，事情还不止于此。想想一本临床操作手册：它可以是关于某项基础常规操作的，复杂度极低；也可以描述一些琐碎事务的步骤，比如怎么正确填写文书，或者怎么处置某种材料。*实践指南可以、确实会、而且常常应当涵盖基础操作。*

  ── [tutorials-how-to]
  EN | At the same time, even as a qualified doctor, you will find yourself back in training situations. Some of them may be very advanced and specialised, requiring a high level of skill and expertise already.
  旧 | 与此同时，即使作为一名合格医生，你仍会发现自己置身于培训情境中。其中一些可能非常先进和专业化，要求使用者已具备相当高的技能与专业知识水平。
  新 | 与此同时，即便已是合格的医生，你仍会发现自己又回到受训的场景里。有些培训非常高级、非常专门，本身就要求你已经具备很高的技能与专业素养。

  ── [tutorials-how-to]
  EN | Let’s say you’re an anaesthetist of many years’ experience, who attends a course: “Difficult neonatal intubations”. The practical part of the course will be a learning experience: a lesson, safely in the hands of the instructors, that will have you performing particular exercises to develop your skills - just as it was when years earlier, you were learning to suture your first wound.
  旧 | 假设你是一位拥有多年经验的麻醉师，参加一门名为“困难新生儿气管插管”的课程：该课程的实践环节将是一次学习经历——在讲师安全指导下的一课，你将在此执行特定练习以提升技能——这正如多年前你学习缝合第一道伤口时的体验一般。
  新 | 假设你是一位从业多年的麻醉师，去上一门课：“困难新生儿气管插管”。课程的实操部分会是一段学习经历：一堂课，安全地交在讲师们手中，让你做特定的练习来提升技能——就像多年前你学着缝合第一道伤口时一样。

  ── [tutorials-how-to]
  EN | The complexity is wholly different though, and so is the baseline of skills required even to participate in the learning experience. But, it’s of the same form, and serves the same kind of need, as that much earlier lesson.
  旧 | 然而，其复杂性截然不同，甚至参与学习体验所需的基础技能门槛也完全不同。不过，它与之前的那一课形式相同，服务于同一种需求。
  新 | 不过，复杂程度完全是另一回事，就连参加这段学习经历所需的技能底线也完全不同。但它的形式，以及它所服务的那一类需求，都和那堂早得多的课一样。

  ── [tutorials-how-to]
  EN | It’s the same in software documentation: a tutorial can present something complex or advanced. And, a how-to guide can cover something that’s basic or well-known. The difference between the two lies in the need they serve: **the user’s study**, or **their work**.
  旧 | 软件文档亦是如此：教程可以呈现复杂或高级的内容；实践指南则可以涵盖基础或广为人知的内容。两者的区别在于其所服务的需求： **用户的学习**，还是 **他们的工作**。
  新 | 软件文档也是如此：教程可以讲复杂或高级的内容，实践指南也可以涵盖基础或众所周知的内容。两者的区别，在于它们各自服务的需求：**用户的学习（学）**，还是**用户的工作（用）**。

  ── [tutorials-how-to]
  EN | Understanding these distinctions, and the reason for upholding them, is crucial to creating successful documentation. A clinical manual that conflated education with practice, that tried to teach while at the same time providing a guide to a real-world procedure would be a literally deadly document. It would kill people.
  旧 | 理解这些区别以及坚持区分的理由，是创建成功文档的关键。一份混淆教学与实践、试图在教导用户的同时又提供现实世界实践指南的临床手册，确实可能成为致命文档——它可能导致人员死亡。
  新 | 理解这些区别，以及坚持这些区别的理由，对于写出成功的文档至关重要。一本把教学与实践混在一起、既想教人又想为现实操作提供指引的临床手册，会是真正致命的文档。它会害死人。

  ── [tutorials-how-to]
  EN | In disciplines such as software documentation, we get away with a great deal, because our conflations and mistakes rarely kill anyone. However, we can cause a great deal of low-level inconvenience and unhappiness to our users, and we add to it, every single time we publish a tutorial or how-to guide that doesn’t understand whether its purpose is to help the user in their study - the acquisition of skills - or in their work - the application of skills.
  旧 | 在软件文档等领域，我们往往能避免严重后果，因为我们的混淆和错误很少会危及任何人。然而，我们确实会给用户带来大量的低级别不便和不快；每当我们发布一份未能明确其目的是服务于 **学（习得）**——帮助用户学习技能，还是服务于 **用（应用）**——帮助用户在工作中运用技能的教程或实践指南时，这种伤害便会增加一分。
  新 | 在软件文档这类领域，我们侥幸躲过了许多，因为我们的混淆和错误很少会闹出人命。然而，我们照样会给用户带来大量低烈度的不便与不快；而且，每当我们发布一份教程或实践指南，却没弄清自己的目的究竟是帮用户学习——即习得技能——还是帮用户工作——即应用技能，这份不快就又多一分。

  ── [tutorials-how-to]
  EN | What’s more, we hurt ourselves too. Users don’t have to use our product. If our documentation doesn’t bring them to success - if it doesn’t meet the needs that they have at a particular stage in their cycle of interaction with our product - they will find something else that does, if they can.
  旧 | 此外，我们也在损害自身。用户并非必须使用我们的产品。如果我们的文档不能让他们成功——不能满足他们在与产品互动的特定阶段所抱有的需求——那么只要他们找得到能满足这些需求的其他东西，就会转向别处。
  新 | 更何况，我们也在伤害自己。用户不是非用我们的产品不可。如果文档不能把他们带向成功——不能满足他们在与产品的交互循环中某一阶段的需求——那么只要找得到别的能满足这些需求的东西，他们就会去找。

  ── [tutorials-how-to]
  EN | The conflation of tutorials and how-to guides is by no means the only one made between different kinds of documentation, but it's one of the easiest to make. It's also a particularly harmful one, because it risks getting in the way of those newcomers whom we hope to turn into committed users. For the sake of those users, and of our own product, getting the distinction right is a key to success.
  旧 | 教程与实践指南的混淆并非不同种类文档之间唯一存在的混淆现象，但它是其中最容易做出的混淆之一。这也是一种特别有害的混淆，因为它有可能妨碍那些我们希望将其转化为忠实用户的新人。为了这些用户的利益，也为了我们的产品自身，正确把握这一区别是取得成功的关键。
  新 | 教程与实践指南的混淆，绝不是各类文档之间唯一的一种混淆，却是最容易犯的一种。它还格外有害，因为它可能挡住那些我们盼着变成忠实用户的新人。为了这些用户，也为了我们自己的产品，把这个区别弄清楚，是成功的关键。

合计：827 条，改动 601 条
