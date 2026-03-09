# 指令

## v-bk-tooltips

用于显示悬停提示的指令。

### 基本用法

```vue
<span v-bk-tooltips="'提示内容'">悬停显示</span>
```

### 配置项

| 配置项 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `content` | String | - | 提示内容 |
| `placement` | String | `'top'` | 位置: `'top'` \| `'bottom'` \| `'left'` \| `'right'` \| `'top-start'` \| `'top-end'` 等 |
| `theme` | String | `'dark'` | 主题: `'dark'` \| `'light'` |
| `delay` | Number \| Array | `[100, 0]` | 显示/隐藏延迟 [显示, 隐藏] |
| `distance` | Number | `10` | 与元素的距离 |
| `maxWidth` | Number | `400` | 最大宽度 |
| `interactive` | Boolean | `false` | 允许与提示框交互 |
| `trigger` | String | `'mouseenter focus'` | 触发事件 |
| `allowHTML` | Boolean | `false` | 允许 HTML 内容 |
| `arrow` | Boolean | `true` | 显示箭头 |
| `boundary` | String | `'window'` | 边界元素 |
| `disabled` | Boolean | `false` | 禁用提示 |
| `zIndex` | Number | - | 自定义 z-index |
| `onShow` | Function | - | 显示回调 |
| `onHide` | Function | - | 隐藏回调 |

### 示例

```vue
<!-- 简单字符串 -->
<span v-bk-tooltips="'简单提示'">悬停显示</span>

<!-- 配置对象 -->
<span v-bk-tooltips="{ content: '底部提示', placement: 'bottom' }">
  悬停显示
</span>

<!-- 动态内容 -->
<span v-bk-tooltips="{ content: dynamicContent }">悬停显示</span>

<!-- 浅色主题 -->
<span v-bk-tooltips="{ content: '浅色主题', theme: 'light' }">
  浅色提示
</span>

<!-- HTML 内容 -->
<span v-bk-tooltips="{ content: '<b>粗体</b>文字', allowHTML: true }">
  HTML 提示
</span>

<!-- 点击触发 -->
<span v-bk-tooltips="{ content: '点击提示', trigger: 'click' }">
  点击显示
</span>

<!-- 动态禁用 -->
<span v-bk-tooltips="{ content: '提示', disabled: isDisabled }">
  条件提示
</span>

<!-- 带回调 -->
<span v-bk-tooltips="{
  content: '提示',
  onShow: () => console.log('已显示'),
  onHide: () => console.log('已隐藏')
}">
  带回调
</span>
```

---

## v-bkloading

加载遮罩指令。

### 基本用法

```vue
<div v-bkloading="isLoading">内容</div>
```

### 配置项

| 配置项 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `isLoading` | Boolean | `false` | 加载状态 |
| `title` | String | `''` | 加载文字 |
| `opacity` | Number | `0.9` | 遮罩透明度 |
| `color` | String | - | 加载图标颜色 |
| `zIndex` | Number | - | 自定义 z-index |
| `size` | String | `'normal'` | 尺寸: `'small'` \| `'normal'` \| `'large'` |
| `mode` | String | `'default'` | 模式: `'default'` \| `'spin'` |
| `delay` | Number | `0` | 显示延迟（ms） |
| `extCls` | String | `''` | 外部 CSS 类名 |
| `afterLeave` | Function | - | 隐藏后回调 |
| `immediate` | Boolean | `false` | 立即显示无动画 |

### 示例

```vue
<!-- 简单布尔值 -->
<div v-bkloading="isLoading">
  需要加载的内容
</div>

<!-- 配置项 -->
<div v-bkloading="{ isLoading: loading, title: '数据加载中...' }">
  内容
</div>

<!-- 自定义样式 -->
<div v-bkloading="{
  isLoading: loading,
  title: '请稍候',
  opacity: 0.7,
  size: 'large'
}">
  内容
</div>

<!-- 旋转模式 -->
<div v-bkloading="{ isLoading: loading, mode: 'spin' }">
  内容
</div>

<!-- 带延迟 -->
<div v-bkloading="{ isLoading: loading, delay: 300 }">
  内容（300ms 后显示加载）
</div>

<!-- 表格加载 -->
<bk-table :data="tableData" v-bkloading="{ isLoading: tableLoading }">
  ...
</bk-table>
```

---

## v-bk-clickoutside

元素外部点击检测指令。

### 基本用法

```vue
<div v-bk-clickoutside="handleClickOutside">
  点击此元素外部触发
</div>
```

### 配置项

传递对象时：

| 配置项 | 类型 | 说明 |
|--------|------|------|
| `handler` | Function | 点击外部时的回调 |
| `isActive` | Boolean | 启用/禁用检测 |
| `exclude` | Array | 要排除的元素选择器 |

### 示例

```vue
<!-- 简单处理器 -->
<div v-bk-clickoutside="closeDropdown">
  下拉内容
</div>

<script>
methods: {
  closeDropdown() {
    this.isOpen = false
  }
}
</script>

<!-- 配置项 -->
<div v-bk-clickoutside="{
  handler: handleClickOutside,
  isActive: isOpen,
  exclude: ['.trigger-btn']
}">
  内容
</div>

<!-- 自定义下拉实现 -->
<div class="dropdown-wrapper">
  <button class="trigger-btn" @click="isOpen = !isOpen">
    切换
  </button>
  <div
    v-if="isOpen"
    v-bk-clickoutside="{
      handler: () => isOpen = false,
      exclude: ['.trigger-btn']
    }"
    class="dropdown-content"
  >
    下拉内容
  </div>
</div>
```

---

## v-bk-overflow-tips

文本溢出时显示提示的指令。

### 基本用法

```vue
<div v-bk-overflow-tips class="ellipsis">
  可能溢出的长文本...
</div>
```

### 配置项

与 `v-bk-tooltips` 相同，另外：

| 配置项 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `content` | String | - | 覆盖内容（默认：元素文本） |

### 示例

```vue
<!-- 自动检测溢出 -->
<div
  v-bk-overflow-tips
  style="width: 100px; overflow: hidden; text-overflow: ellipsis; white-space: nowrap;"
>
  这是一段会溢出的很长的文本
</div>

<!-- 配置项 -->
<div
  v-bk-overflow-tips="{ placement: 'bottom', theme: 'light' }"
  class="ellipsis-text"
>
  长文本内容
</div>

<!-- 表格列中使用 -->
<bk-table-column prop="description" label="描述">
  <template slot-scope="{ row }">
    <span v-bk-overflow-tips class="ellipsis">
      {{ row.description }}
    </span>
  </template>
</bk-table-column>
```

**CSS 辅助类:**
```css
.ellipsis {
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}
```

---

## v-bk-copy

复制到剪贴板指令。

### 基本用法

```vue
<span v-bk-copy="textToCopy">点击复制</span>
```

### 配置项

| 配置项 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `value` | String | - | 要复制的文本 |
| `successMessage` | String | `'复制成功'` | 成功消息 |
| `errorMessage` | String | `'复制失败'` | 失败消息 |

### 示例

```vue
<!-- 简单复制 -->
<bk-button v-bk-copy="'要复制的文本'">
  复制文本
</bk-button>

<!-- 动态值 -->
<bk-button v-bk-copy="dynamicText">
  复制 {{ dynamicText }}
</bk-button>

<!-- 自定义消息 -->
<bk-button v-bk-copy="{
  value: textToCopy,
  successMessage: '已复制！',
  errorMessage: '复制失败'
}">
  复制
</bk-button>

<!-- 复制输入框值 -->
<bk-input v-model="inputValue" />
<bk-button v-bk-copy="inputValue">复制输入内容</bk-button>

<!-- 复制代码片段 -->
<pre>
  <code>{{ codeSnippet }}</code>
  <bk-button
    v-bk-copy="codeSnippet"
    text
    size="small"
    icon="icon-copy"
  />
</pre>
```

---

## v-bk-resize

元素尺寸变化检测指令。

### 基本用法

```vue
<div v-bk-resize="handleResize">
  可调整大小的内容
</div>
```

### 处理器参数

```javascript
handleResize(entry) {
  // entry 是 ResizeObserverEntry
  const { width, height } = entry.contentRect
  console.log('新尺寸:', width, height)
}
```

### 示例

```vue
<!-- 基础尺寸检测 -->
<div v-bk-resize="handleResize" class="resizable-container">
  内容
</div>

<script>
methods: {
  handleResize(entry) {
    const { width, height } = entry.contentRect
    this.containerWidth = width
    this.containerHeight = height
  }
}
</script>

<!-- 响应式组件 -->
<div v-bk-resize="onContainerResize" class="responsive-wrapper">
  <component :is="responsiveComponent" />
</div>

<script>
methods: {
  onContainerResize(entry) {
    const { width } = entry.contentRect
    if (width < 600) {
      this.responsiveComponent = 'MobileView'
    } else {
      this.responsiveComponent = 'DesktopView'
    }
  }
}
</script>

<!-- 图表尺寸调整 -->
<div v-bk-resize="resizeChart" class="chart-container">
  <canvas ref="chart"></canvas>
</div>

<script>
methods: {
  resizeChart(entry) {
    const { width, height } = entry.contentRect
    this.chart.resize(width, height)
  }
}
</script>
```

---

## 指令注册

全量引入组件库时，所有指令会自动注册：

```javascript
import Vue from 'vue'
import bkMagicVue from '@canway/cw-magic-vue'

Vue.use(bkMagicVue)
```

按需引入：

```javascript
import { bkTooltips, bkLoading, bkClickoutside, bkOverflowTips, bkCopy } from '@canway/cw-magic-vue'

Vue.directive('bk-tooltips', bkTooltips)
Vue.directive('bkloading', bkLoading)
Vue.directive('bk-clickoutside', bkClickoutside)
Vue.directive('bk-overflow-tips', bkOverflowTips)
Vue.directive('bk-copy', bkCopy)
```

---

## 常用模式

### 表格加载与空状态

```vue
<div v-bkloading="{ isLoading: loading }">
  <bk-table :data="tableData">
    ...
  </bk-table>
  <bk-exception v-if="!loading && !tableData.length" type="empty" scene="part">
    暂无数据
  </bk-exception>
</div>
```

### 表格中溢出提示

```vue
<bk-table-column prop="name" label="名称">
  <template slot-scope="{ row }">
    <span
      v-bk-overflow-tips
      style="display: block; overflow: hidden; text-overflow: ellipsis; white-space: nowrap;"
    >
      {{ row.name }}
    </span>
  </template>
</bk-table-column>
```

### 复制按钮带反馈

```vue
<div class="code-block">
  <pre>{{ code }}</pre>
  <bk-button
    v-bk-copy="{ value: code, successMessage: '代码已复制！' }"
    text
    size="small"
  >
    <i class="bk-icon icon-copy"></i>
  </bk-button>
</div>
```

### 自定义下拉与外部点击

```vue
<div class="custom-dropdown">
  <bk-button @click="isOpen = !isOpen">
    {{ selected || '请选择' }} <i class="bk-icon icon-angle-down"></i>
  </bk-button>
  <ul
    v-if="isOpen"
    v-bk-clickoutside="() => isOpen = false"
    class="dropdown-list"
  >
    <li v-for="item in options" :key="item.id" @click="selectItem(item)">
      {{ item.name }}
    </li>
  </ul>
</div>
```
