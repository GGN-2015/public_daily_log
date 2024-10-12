# 《关于 MCVR 实验室网站的心路历程》

## 置顶信息

- 如何构建：

```bash
rm -f ./layouts/_default/baseof.html
hugo --cleanDestinationDir # 无视报错
hugo                       # 无视报错
touch ./layouts/_default/baseof.html
hugo                            # 没有报错
hugo server --disableFastRender # 没有报错
```

- 注意事项
  - 每次 pull request 合并之后需要手动运行一次

## 2024-10

- `2024-10-01` 终于抽出时间来搞这个了，争取今天一天之内把所有信息录入完成。
- `2024-10-01` 全部录入完成之后一定要再抽出时间来校对信息的正确性。
- `2024-10-01` 每次提 PR 之前一定要记得现删除空 `baseof.html` 文件
  - `rm ./layouts/_default/baseof.html`
- `2024-10-01` 诶，github 上的构建脚本挂了？为什么我本地看起来没问题的网站 github 上面构建的系统却使用了原始的 README.md 作为主页。
  - 试图把空的 `baseof.html` 放上去，并且将 github 上的 hugo 版本与我本地的 hugo 版本设置为一致
  - 结果效果还是不对，github pages 上看到的总是 README.md 页面作为主页
  - 我想想主页来源于哪里？
  - 好，我一顿爆改 github actions 然后让他在构建失败的条件下也能 deploy
  - 用这种极其扭曲的方式实现了构建
  - 我个人觉得正确的做法压根就不应该用这种 out dated 的框架，我觉得应该会有这个框架的新版本内容使得不再有 .Site.Google 的问题
  - 但是既然现在以这种扭曲的方式解决了问题，总之还是比没有解决要好的
    - 以后出了锅以后再说
    - **长久之计应该是用一个新一点的模板**
- `2024-10-01` 好，现在我回来研究怎么怎么加文献上去
  - 所有文献位于 `./content/publication` 每个文献占据一个文件夹
  - 其中可以提供，代码链接，数据集链接，视频，BibTex Citation，等等内容
  - 感觉工作量也不小，打算先把在校生发表的论文整理出来
- `2024-10-01` 行，今天先干到这里，整理一下工作进度
  - 完成了在校生的论文整理工作
  - 其中还有若干个本地视频文件，我想想有没有什么比较合适的处理思路（毕竟把视频放到 github repo 里不太合适）
  - 还有很多毕业生的工作需要整理
  - 还没有做对照片的检查工作
  - 还没有得到每个人的邮箱
- `2024-10-04` 计划今天把所有的论文先整理上去，视频以后再想想办法怎么搞
  - 对了，之后还得想一下作者辅助信息是不是应该统一加一下
  - 先整理到 meijia-huang，还有 12  篇文章要录入，歇会
- `2024-10-06` 计划今天把所有的论文整理上去。
  - 好，完工了。
- `2024-10-12` 上传了三个在校生视频到 youtube.

## 2024-09

- `2024-09-25` YP 老师让我维护实验室的 github pages
  - 网站：https://vr-pan-junjun.github.io/
  - 仓库：https://github.com/vr-pan-junjun/vr-pan-junjun.github.io
  - 既然 YP 老师没有给我协作者，那我就 fork 一个然后提 PR 吧
  - 仓库：https://github.com/GGN-2015/vr-pan-junjun.github.io

- `2024-09-25` 去看一下 Hugo 的教程
  - 网址：https://docs.hugoblox.com/tutorial/
  - 感谢 YP 老师给的文档：https://docs.hugoblox.com/getting-started/install-hugo/

- `2024-09-25` 心路路程
  - 使用 `oma install hugo` 安装了 hugo
  - 在项目目录下执行 `hugo server --logLevel info` 遇到了报错
    - WARN  deprecated: site config key paginate was deprecated in Hugo v0.128.0 and will be removed in a future release. Use pagination.pagerSize instead.
      - 这个好解决，在 `hugo.yaml` 里改一下就行。
    - ERROR deprecated: .Site.GoogleAnalytics was deprecated in Hugo v0.120.0 and will be removed in Hugo 0.135.0. Use .Site.Config.Services.GoogleAnalytics.ID instead.
  - 我猜这个 `.Site.Config.Services.GoogleAnalytics.ID` 可能是和检索相关的东西吧，去掉应该问题不大？我找找。
    - 我把 `params.yaml` 里的 `analytics` 中对应的项目删了
      - 但是还是不能正常工作
      - 所以我估计应该是主题导致的，我打算去主题对应的 github 页面看看
      - 他是个 template 连 issue 都提不了，自闭
    - 考虑到统计代码往往都是写在 paritals 的
      - 读一下，感觉我代码里也没有 partial 块啊？https://gohugo.io/templates/partial/
      - 好耶，解决了，做法是新建了空的 `baseof.html` 文件
        - 这东西缺省项里有 lagecy 东西也不告诉我一声，我真的好惨
        - 研究两个多小时终于解决了
- `2024-09-25` 然后就可以向项目里面填写东西了
  - 人相关的信息都在 `./content/en/authors/` 目录下
  - 我发现我加人/修改后重新编译项目，网站看起来一点变化都没有
  - `hugo --cleanDestinationDir` 之后再 `hugo server`
  - 结果就是打开就是 page not found
  - `hugo server --disableFastRender` 还是不行
  - 我以为是 git 子模块的问题，但看了一眼这个项目压根就没有子模块？（那您主题怎么导入的？？？？）
  - 莫名其妙就好使了？难道真的是子模块的问题？？？没有子模块啊？

- `2024-09-25` 好，既然能用了，那我就按一下的的顺序处理了
  - 第一步，把所有学生的名字填了
  - 第二步，挨个填他们的代表作
  - 最后，如果可能的话最好把每个人的邮箱找到
  - 诶，感觉还是不能让 people 根页面自动把 author 文件夹里的子目录导入进去
    - 哦哦，可能就是 `--disableFastRender` 吧
    - 理解了，每次 `hugo --cleanDestinationDir` 后必然导致 `page not found` 的问题
    - 但是刚才他怎么就好使了啊，自闭，我没觉得我做了任何操作啊？
  - 我靠我终于复现出来了，流程是这样的
    - 首先，删掉文件 `baseof.html`
    - 然后执行 `hugo`，这个时候会有 google analysis 的那个报错
    - 但是没关系，现在我们重新把 `baseof.html` 文件塞回去
    - 再执行 `hugo server --disableFastRender` 后能看到正常的页面
  - 让我分析一下到底发生了什么
    - 这里我们假说演绎法一下（因为看不到 hugo 的源代码）
    - 我分析很可能是因为缺省的 `baseof.html` 中使用了 lagecy 的语法调用了 `google analysis`
    - 我们创建了空白的 `baseof.html` 由于是空白的，所以绕过了 `google analysis` 的 error deprecated
    - 但是由于 `baseof.html` 中没有实际内容是不行的，所以在这种状态下无法构建 html
  - 所以真正能够解决问题的方式应当是找到那个默认的 `baseof.html` 的缺省实现，然后去把里面有问题的东西修改了
    - `baseof.html` 是主体相关的，但是我并没有在这个项目内看到任何主题声明
    - 自闭
    - 所以在这个问题彻底解决之前我先再填几个学生的信息上去吧

- `2024-09-25` 回到先前的工作流
  - 第一步，把所有学生的名字填了
  - 第二步，挨个填他们的代表作
  - 最后，如果可能的话最好把每个人的邮箱找到

- `2024-09-25` 给出一条可供参考的本地启动路线

```bash
rm -f ./layouts/_default/baseof.html
hugo --cleanDestinationDir # 无视报错
hugo                       # 无视报错
touch ./layouts/_default/baseof.html
hugo                            # 没有报错
hugo server --disableFastRender # 没有报错
```

- `2024-09-25` 好现在所有姓名填写完了，之后还要写毕业去向，代表作，个人邮箱
  - 先 merge 一个 pull request，在官网上看效果是正确的
  - 洗个澡吧，感觉再搞下去人都要自闭了

