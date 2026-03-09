# Layout Components

## Container (bk-container)

Flexible container component for layout management.

### Props

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `col` | Number | `24` | Total columns in grid system |
| `gutter` | Number | `0` | Gutter spacing (px) |
| `margin` | Number | `20` | Container margin (px) |
| `flex` | Boolean | `false` | Use flexbox layout |
| `extCls` | String | `''` | External CSS class |

### Slots

| Slot | Description |
|------|-------------|
| `default` | Container content (rows or content) |

### Examples

```vue
<bk-container :gutter="20">
  <bk-row>
    <bk-col :span="12">Left half</bk-col>
    <bk-col :span="12">Right half</bk-col>
  </bk-row>
</bk-container>

<!-- Flex container -->
<bk-container flex>
  <bk-row>
    <bk-col :span="8">1/3</bk-col>
    <bk-col :span="8">1/3</bk-col>
    <bk-col :span="8">1/3</bk-col>
  </bk-row>
</bk-container>
```

---

## Row (bk-row)

Grid row component.

### Props

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `gutter` | Number | `0` | Gutter spacing (px) |
| `flex` | Boolean | `false` | Use flexbox layout |
| `justify` | String | `'start'` | Horizontal alignment: `'start'` \| `'end'` \| `'center'` \| `'space-around'` \| `'space-between'` |
| `align` | String | `'top'` | Vertical alignment: `'top'` \| `'middle'` \| `'bottom'` |
| `extCls` | String | `''` | External CSS class |

### Slots

| Slot | Description |
|------|-------------|
| `default` | Row content (columns) |

### Examples

```vue
<bk-row :gutter="20">
  <bk-col :span="8">Column 1</bk-col>
  <bk-col :span="8">Column 2</bk-col>
  <bk-col :span="8">Column 3</bk-col>
</bk-row>

<!-- Flex alignment -->
<bk-row flex justify="center" align="middle">
  <bk-col :span="6">Centered</bk-col>
</bk-row>

<!-- Space between -->
<bk-row flex justify="space-between">
  <bk-col :span="4">Left</bk-col>
  <bk-col :span="4">Center</bk-col>
  <bk-col :span="4">Right</bk-col>
</bk-row>
```

---

## Col (bk-col)

Grid column component.

### Props

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `span` | Number | `24` | Column span (1-24) |
| `offset` | Number | `0` | Offset columns |
| `pull` | Number | `0` | Pull columns (move left) |
| `push` | Number | `0` | Push columns (move right) |
| `extCls` | String | `''` | External CSS class |

### Responsive Props

| Prop | Type | Description |
|------|------|-------------|
| `xs` | Number \| Object | `<768px` responsive config |
| `sm` | Number \| Object | `≥768px` responsive config |
| `md` | Number \| Object | `≥992px` responsive config |
| `lg` | Number \| Object | `≥1200px` responsive config |
| `xl` | Number \| Object | `≥1920px` responsive config |

Object format: `{ span, offset, pull, push }`

### Slots

| Slot | Description |
|------|-------------|
| `default` | Column content |

### Examples

```vue
<!-- Basic columns -->
<bk-row :gutter="20">
  <bk-col :span="6">6/24</bk-col>
  <bk-col :span="6">6/24</bk-col>
  <bk-col :span="6">6/24</bk-col>
  <bk-col :span="6">6/24</bk-col>
</bk-row>

<!-- With offset -->
<bk-row>
  <bk-col :span="8">8</bk-col>
  <bk-col :span="8" :offset="8">8 with offset 8</bk-col>
</bk-row>

<!-- Responsive -->
<bk-row :gutter="20">
  <bk-col :xs="24" :sm="12" :md="8" :lg="6">
    Responsive column
  </bk-col>
  <bk-col :xs="24" :sm="12" :md="8" :lg="6">
    Responsive column
  </bk-col>
</bk-row>

<!-- Responsive with full config -->
<bk-row>
  <bk-col :xs="{ span: 24 }" :sm="{ span: 12, offset: 6 }">
    Complex responsive
  </bk-col>
</bk-row>
```

---

## ResizeLayout (bk-resize-layout)

Resizable split layout component.

### Props

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `placement` | String | `'left'` | Resizable panel position: `'left'` \| `'right'` \| `'top'` \| `'bottom'` |
| `min` | Number | `100` | Minimum panel size (px) |
| `max` | Number | `500` | Maximum panel size (px) |
| `initialDivide` | Number \| String | `'50%'` | Initial divide position |
| `disabled` | Boolean | `false` | Disable resize |
| `immediate` | Boolean | `false` | Immediate resize (vs resize on release) |
| `border` | Boolean | `true` | Show border on divider |
| `collapsible` | Boolean | `false` | Enable collapse |
| `collapsed` | Boolean | `false` | Collapsed state (supports .sync) |
| `autoMinimize` | Boolean | `true` | Auto minimize when too small |
| `extCls` | String | `''` | External CSS class |

### Events

| Event | Parameters | Description |
|-------|------------|-------------|
| `resize` | `(size: Number)` | Emitted during resize |
| `resizing` | `(size: Number)` | Emitted continuously during resize |
| `resize-start` | - | Emitted when resize starts |
| `resize-end` | - | Emitted when resize ends |
| `collapse` | - | Emitted when panel collapsed |
| `expand` | - | Emitted when panel expanded |
| `update:collapsed` | `(collapsed: Boolean)` | Emitted for .sync modifier |
| `before-resize` | `(size: Number)` | Emitted before resize (return false to cancel) |

### Slots

| Slot | Description |
|------|-------------|
| `aside` | Resizable panel content |
| `main` | Main content |
| `collapse-trigger` | Custom collapse trigger |

### Examples

```vue
<!-- Basic horizontal split -->
<bk-resize-layout :min="200" :max="600" initial-divide="300px">
  <template slot="aside">
    <div class="sidebar">Sidebar content</div>
  </template>
  <template slot="main">
    <div class="main-content">Main content</div>
  </template>
</bk-resize-layout>

<!-- Right placement -->
<bk-resize-layout placement="right" :min="200" :max="400">
  <template slot="aside">
    <div class="right-panel">Right Panel</div>
  </template>
  <template slot="main">
    <div class="main-content">Main</div>
  </template>
</bk-resize-layout>

<!-- Vertical split (top/bottom) -->
<bk-resize-layout placement="top" :min="100" :max="300">
  <template slot="aside">
    <div class="top-panel">Top Panel</div>
  </template>
  <template slot="main">
    <div class="bottom-content">Bottom Content</div>
  </template>
</bk-resize-layout>

<!-- Collapsible -->
<bk-resize-layout
  :min="200"
  :max="400"
  collapsible
  :collapsed.sync="isCollapsed"
>
  <template slot="aside">
    <div class="sidebar">Collapsible Sidebar</div>
  </template>
  <template slot="main">
    <div class="main-content">Main Content</div>
  </template>
</bk-resize-layout>

<!-- Nested layouts -->
<bk-resize-layout :min="200" :max="600" initial-divide="250px">
  <template slot="aside">
    <div class="left-sidebar">Left</div>
  </template>
  <template slot="main">
    <bk-resize-layout placement="right" :min="200" :max="400">
      <template slot="aside">
        <div class="right-sidebar">Right</div>
      </template>
      <template slot="main">
        <div class="center-content">Center</div>
      </template>
    </bk-resize-layout>
  </template>
</bk-resize-layout>
```

---

## Grid System Overview

The grid system uses a 24-column layout by default.

### Breakpoints

| Breakpoint | Size | Class prefix |
|------------|------|--------------|
| xs | `<768px` | Extra small (mobile) |
| sm | `≥768px` | Small (tablet) |
| md | `≥992px` | Medium (desktop) |
| lg | `≥1200px` | Large (large desktop) |
| xl | `≥1920px` | Extra large |

### Common Patterns

```vue
<!-- Two column layout -->
<bk-row :gutter="20">
  <bk-col :span="16">Main Content</bk-col>
  <bk-col :span="8">Sidebar</bk-col>
</bk-row>

<!-- Three column layout -->
<bk-row :gutter="20">
  <bk-col :span="8">Left</bk-col>
  <bk-col :span="8">Center</bk-col>
  <bk-col :span="8">Right</bk-col>
</bk-row>

<!-- Responsive card grid -->
<bk-row :gutter="20">
  <bk-col
    v-for="item in items"
    :key="item.id"
    :xs="24"
    :sm="12"
    :md="8"
    :lg="6"
  >
    <bk-card :title="item.title">{{ item.content }}</bk-card>
  </bk-col>
</bk-row>

<!-- Form layout -->
<bk-row :gutter="20">
  <bk-col :span="12">
    <bk-form-item label="Field 1">
      <bk-input />
    </bk-form-item>
  </bk-col>
  <bk-col :span="12">
    <bk-form-item label="Field 2">
      <bk-input />
    </bk-form-item>
  </bk-col>
</bk-row>
```
