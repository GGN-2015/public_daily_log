# 《关于实验室网站》

## 2024-09

- `2024-09-25` YP 老师让我维护实验室的 github pages
  - 网站：https://vr-pan-junjun.github.io/
  - 仓库：https://github.com/vr-pan-junjun/vr-pan-junjun.github.io
  - 既然 YP 老师没有给我协作者，那我就 fork 一个然后提 PR 吧
  - 仓库：https://github.com/GGN-2015/vr-pan-junjun.github.io

- `2024-09-25` 去看一下 Hugo 的教程
  - 网址：https://docs.hugoblox.com/tutorial/
  - YP 老师给的文档：https://docs.hugoblox.com/getting-started/install-hugo/

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

