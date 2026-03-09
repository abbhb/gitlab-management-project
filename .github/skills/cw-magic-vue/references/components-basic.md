# 基础组件

## Button 按钮 (bk-button)

基础按钮组件，支持多种主题、尺寸和状态。

### 属性

| 属性 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| `theme` | String | `'default'` | 按钮主题: `'default'` \| `'primary'` \| `'warning'` \| `'success'` \| `'danger'` |
| `hoverTheme` | String | `''` | 悬停主题（覆盖 `theme` 和 `text`）: `''` \| `'primary'` \| `'warning'` \| `'success'` \| `'danger'` |
| `size` | String | `'normal'` | 按钮尺寸: `'mini'` \| `'small'` \| `'normal'` \| `'large'` |
| `title` | String | `''` | 按钮 title 提示 |
| `icon` | String | - | 左侧图标类名（如 `'icon-plus'`）。使用 `'loading'` 显示旋转效果 |
| `iconRight` | String | - | 右侧图标类名 |
| `disabled` | Boolean | `false` | 禁用按钮 |
| `loading` | Boolean | `false` | 显示加载状态 |
| `useRingLoading` | Boolean | `false` | 使用圆环加载动画代替弹跳动画 |
| `outline` | Boolean | `false` | 显示描边/幽灵样式 |
| `text` | Boolean | `false` | 显示为文字按钮（无背景） |
| `border` | Boolean | `true` | 显示边框 |
| `nativeType` | String | `'button'` | 原生按钮类型: `'button'` \| `'submit'` \| `'reset'` |
| `extCls` | String | `''` | 外部 CSS 类名 |

### 事件

| 事件 | 参数 | 说明 |
|------|------|------|
| `click` | `(event: MouseEvent)` | 点击按钮时触发（禁用/加载时不触发） |

### 插槽

| 插槽 | 说明 |
|------|------|
| `default` | 按钮文本内容 |
| `left-icon` | 自定义左侧图标 |
| `right-icon` | 自定义右侧图标 |

### 示例

```vue
<!-- 基础按钮 -->
<bk-button>默认</bk-button>
<bk-button theme="primary">主要</bk-button>
<bk-button theme="success">成功</bk-button>
<bk-button theme="warning">警告</bk-button>
<bk-button theme="danger">危险</bk-button>

<!-- 尺寸 -->
<bk-button size="mini">迷你</bk-button>
<bk-button size="small">小</bk-button>
<bk-button size="normal">正常</bk-button>
<bk-button size="large">大</bk-button>

<!-- 状态 -->
<bk-button disabled>禁用</bk-button>
<bk-button loading>加载中</bk-button>
<bk-button loading use-ring-loading>圆环加载</bk-button>

<!-- 样式 -->
<bk-button theme="primary" outline>描边</bk-button>
<bk-button theme="primary" text>文字按钮</bk-button>

<!-- 带图标 -->
<bk-button icon="icon-plus">添加</bk-button>
<bk-button icon-right="icon-angle-right">下一步</bk-button>
<bk-button icon="icon-plus" icon-right="icon-angle-right">双图标</bk-button>

<!-- 悬停主题 -->
<bk-button hover-theme="primary">悬停变主色</bk-button>
```

---

## Icon 图标 (bk-icon)

图标组件，支持图标字体和 SVG 符号。

### 属性

| 属性 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| `type` | String | **必填** | 图标名称（不含前缀） |
| `svg` | Boolean | `false` | 使用 SVG 符号代替图标字体 |
| `width` | String | `'1em'` | SVG 宽度（仅当 `svg: true`） |
| `height` | String | `'1em'` | SVG 高度（仅当 `svg: true`） |
| `size` | String | `'inherit'` | 字体大小 |

### 示例

```vue
<!-- 图标字体 -->
<bk-icon type="close" />
<bk-icon type="search" size="20px" />
<bk-icon type="plus" size="24px" />

<!-- SVG 符号 -->
<bk-icon type="custom-icon" svg />
<bk-icon type="custom-icon" svg width="24px" height="24px" />

<!-- 直接使用类名（替代方式） -->
<i class="bk-icon icon-close"></i>
<i class="bk-icon icon-search" style="font-size: 20px;"></i>
```

### 常用图标名称

- 导航: `angle-left`, `angle-right`, `angle-up`, `angle-down`, `arrows-left`, `arrows-right`
- 操作: `plus`, `minus`, `close`, `check-1`, `edit`, `delete`, `refresh`, `search`
- 状态: `info`, `warning`, `success`, `error`, `help`
- 文件: `file`, `folder`, `upload`, `download`
- 其他: `user`, `setting`, `eye`, `eye-slash`, `copy`, `link`

---

## Link 链接 (bk-link)

带主题支持的超链接组件。

### 属性

| 属性 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| `theme` | String | `'default'` | 链接主题: `'default'` \| `'primary'` \| `'success'` \| `'warning'` \| `'danger'` |
| `href` | String | `null` | 链接 URL |
| `disabled` | Boolean | `false` | 禁用链接 |
| `underline` | Boolean | `false` | 悬停时显示下划线 |
| `icon` | String | - | 图标类名 |
| `iconPlacement` | String | `'left'` | 图标位置: `'left'` \| `'right'` |

### 事件

| 事件 | 参数 | 说明 |
|------|------|------|
| `click` | `(event: MouseEvent)` | 点击链接时触发 |

### 插槽

| 插槽 | 说明 |
|------|------|
| `default` | 链接文本内容 |

### 示例

```vue
<!-- 基础链接 -->
<bk-link href="https://example.com">默认链接</bk-link>
<bk-link theme="primary" href="/page">主要链接</bk-link>
<bk-link theme="success">成功链接</bk-link>
<bk-link theme="warning">警告链接</bk-link>
<bk-link theme="danger">危险链接</bk-link>

<!-- 带下划线 -->
<bk-link underline href="/page">悬停下划线</bk-link>

<!-- 禁用 -->
<bk-link disabled>禁用链接</bk-link>

<!-- 带图标 -->
<bk-link icon="bk-icon icon-link">左侧图标</bk-link>
<bk-link icon="bk-icon icon-link" icon-placement="right">右侧图标</bk-link>
```

---

## Tag 标签 (bk-tag)

标签组件，用于标记、状态指示和可选项。

### 属性

| 属性 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| `theme` | String | `''` | 标签主题: `''` \| `'success'` \| `'info'` \| `'warning'` \| `'danger'` |
| `type` | String | `''` | 标签类型: `''` \| `'filled'` \| `'stroke'` |
| `size` | String | `''` | 标签尺寸: `''` \| `'large'` \| `'medium'` \| `'small'` |
| `closable` | Boolean | `false` | 显示关闭按钮 |
| `checkable` | Boolean | `false` | 启用选择模式 |
| `checked` | Boolean | `false` | 选中状态（当 `checkable: true`） |
| `icon` | String | `''` | 图标类名 |
| `radius` | String | `'2px'` | 圆角 |
| `border` | Boolean | `false` | 显示边框 |
| `state` | Boolean | `false` | 是否为状态标签 |
| `loading` | Boolean | `false` | 显示加载中 |
| `disabled` | Boolean | `true` | 禁用点击事件 |
| `extCls` | String | `''` | 外部 CSS 类名 |

### 事件

| 事件 | 参数 | 说明 |
|------|------|------|
| `click` | `(event: MouseEvent)` | 点击标签时触发 |
| `close` | `(event: MouseEvent)` | 点击关闭按钮时触发 |
| `change` | `(checked: Boolean)` | 可选状态变化时触发 |

### 插槽

| 插槽 | 说明 |
|------|------|
| `default` | 标签内容 |

### 示例

```vue
<!-- 基础标签 -->
<bk-tag>默认</bk-tag>
<bk-tag theme="success">成功</bk-tag>
<bk-tag theme="info">信息</bk-tag>
<bk-tag theme="warning">警告</bk-tag>
<bk-tag theme="danger">危险</bk-tag>

<!-- 类型 -->
<bk-tag theme="primary" type="filled">填充</bk-tag>
<bk-tag theme="primary" type="stroke">描边</bk-tag>

<!-- 可关闭 -->
<bk-tag closable @close="handleClose">可关闭标签</bk-tag>

<!-- 可选择 -->
<bk-tag checkable :checked="isChecked" @change="handleChange">可选择</bk-tag>

<!-- 带图标 -->
<bk-tag icon="bk-icon icon-user">用户</bk-tag>

<!-- 尺寸 -->
<bk-tag size="small">小</bk-tag>
<bk-tag size="medium">中</bk-tag>
<bk-tag size="large">大</bk-tag>
```

---

## Badge 徽章 (bk-badge)

徽章组件，用于显示数量或状态指示。

### 属性

| 属性 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| `theme` | String | `''` | 徽章主题: `'primary'` \| `'info'` \| `'warning'` \| `'danger'` \| `'success'` 或十六进制颜色 |
| `val` | Number \| String | `1` | 显示值 |
| `valLength` | Number \| String | `3` | 最大显示长度 |
| `max` | Number | `-1` | 最大值（超过显示 `val+`，-1 表示无限制） |
| `icon` | String | `''` | 显示图标（覆盖 `val`） |
| `dot` | Boolean | `false` | 仅显示为小圆点 |
| `visible` | Boolean | `true` | 是否显示徽章 |
| `position` | String | `'top-right'` | 位置: `'top-right'` \| `'bottom-right'` \| `'bottom-left'` \| `'top-left'` |
| `radius` | String \| Number | - | 圆角（0 为方形） |
| `extCls` | String | `''` | 外部 CSS 类名 |

### 事件

| 事件 | 参数 | 说明 |
|------|------|------|
| `hover` | - | 鼠标移入时触发 |
| `leave` | - | 鼠标移出时触发 |

### 插槽

| 插槽 | 说明 |
|------|------|
| `default` | 包裹内容（徽章作为叠加层显示） |

### 示例

```vue
<!-- 基础徽章 -->
<bk-badge :val="5">
  <bk-button>消息</bk-button>
</bk-badge>

<!-- 带最大值 -->
<bk-badge :val="100" :max="99">
  <bk-button>通知</bk-button>
</bk-badge>

<!-- 圆点徽章 -->
<bk-badge dot>
  <bk-button>更新</bk-button>
</bk-badge>

<!-- 主题 -->
<bk-badge :val="5" theme="primary">主要</bk-badge>
<bk-badge :val="5" theme="success">成功</bk-badge>
<bk-badge :val="5" theme="warning">警告</bk-badge>
<bk-badge :val="5" theme="danger">危险</bk-badge>

<!-- 位置 -->
<bk-badge :val="5" position="top-left">左上</bk-badge>
<bk-badge :val="5" position="bottom-right">右下</bk-badge>

<!-- 图标徽章 -->
<bk-badge icon="bk-icon icon-info">
  <span>信息</span>
</bk-badge>
```

---

## Divider 分割线 (bk-divider)

用于分隔内容的视觉分割线。

### 属性

| 属性 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| `direction` | String | `'horizontal'` | 方向: `'horizontal'` \| `'vertical'` |
| `align` | String | `'center'` | 内容对齐: `'left'` \| `'center'` \| `'right'` |
| `color` | String | `'var(--divider-border-color)'` | 分割线颜色 |
| `width` | Number | `1` | 分割线粗细（px） |
| `type` | String | `'solid'` | 边框样式: `'solid'` \| `'dashed'` \| `'dotted'` |

### 插槽

| 插槽 | 说明 |
|------|------|
| `default` | 水平分割线中的内容（创建带文字的间隔） |

### 示例

```vue
<!-- 基础水平分割线 -->
<bk-divider />

<!-- 带文字 -->
<bk-divider>或</bk-divider>
<bk-divider align="left">章节标题</bk-divider>
<bk-divider align="right">结束</bk-divider>

<!-- 垂直分割线 -->
<span>项目 1</span>
<bk-divider direction="vertical" />
<span>项目 2</span>

<!-- 自定义样式 -->
<bk-divider type="dashed" />
<bk-divider type="dotted" color="#ccc" />
<bk-divider :width="2" color="#3a84ff" />
```
