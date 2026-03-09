# Data Display Components

## Table (bk-table)

Data table component with sorting, filtering, selection, and pagination.

### Props

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `data` | Array | `[]` | Table data |
| `height` | Number \| String | - | Table height (enables virtual scroll) |
| `maxHeight` | Number \| String | - | Maximum table height |
| `rowKey` | String \| Function | - | Row key field or function |
| `stripe` | Boolean | `false` | Striped rows |
| `border` | Boolean | `false` | Show border |
| `outerBorder` | Boolean | `false` | Show outer border |
| `rowBorder` | Boolean | `true` | Show row border |
| `colBorder` | Boolean | `false` | Show column border |
| `size` | String | `'small'` | Size: `'small'` \| `'medium'` \| `'large'` |
| `fit` | Boolean | `true` | Fit container width |
| `showHeader` | Boolean | `true` | Show header |
| `highlightCurrentRow` | Boolean | `false` | Highlight current row |
| `rowClassName` | Function \| String | - | Custom row class |
| `rowStyle` | Function \| Object | - | Custom row style |
| `cellClassName` | Function \| String | - | Custom cell class |
| `cellStyle` | Function \| Object | - | Custom cell style |
| `headerRowClassName` | Function \| String | - | Custom header row class |
| `headerRowStyle` | Function \| Object | - | Custom header row style |
| `headerCellClassName` | Function \| String | - | Custom header cell class |
| `headerCellStyle` | Function \| Object | - | Custom header cell style |
| `emptyText` | String | `'暂无数据'` | Empty state text |
| `defaultExpandAll` | Boolean | `false` | Expand all rows by default |
| `expandRowKeys` | Array | - | Expanded row keys |
| `defaultSort` | Object | - | Default sort `{ prop, order }` |
| `tooltipEffect` | String | `'dark'` | Tooltip theme |
| `showSummary` | Boolean | `false` | Show summary row |
| `sumText` | String | `'合计'` | Summary row label |
| `summaryMethod` | Function | - | Custom summary method |
| `spanMethod` | Function | - | Row/column span method |
| `selectOnIndeterminate` | Boolean | `true` | Select all on indeterminate |
| `pagination` | Object | - | Pagination config `{ current, count, limit }` |
| `showOverflowTooltip` | Boolean | `false` | Show tooltip on overflow |
| `immediatelySetRowExpansion` | Boolean | `true` | Immediately set row expansion |
| `extCls` | String | `''` | External CSS class |

### Events

| Event | Parameters | Description |
|-------|------------|-------------|
| `select` | `(selection, row)` | Emitted on row selection change |
| `select-all` | `(selection)` | Emitted on select all toggle |
| `selection-change` | `(selection)` | Emitted when selection changes |
| `cell-mouse-enter` | `(row, column, cell, event)` | Emitted on cell mouseenter |
| `cell-mouse-leave` | `(row, column, cell, event)` | Emitted on cell mouseleave |
| `cell-click` | `(row, column, cell, event)` | Emitted on cell click |
| `cell-dblclick` | `(row, column, cell, event)` | Emitted on cell double-click |
| `row-click` | `(row, column, event)` | Emitted on row click |
| `row-contextmenu` | `(row, column, event)` | Emitted on row right-click |
| `row-dblclick` | `(row, column, event)` | Emitted on row double-click |
| `header-click` | `(column, event)` | Emitted on header click |
| `header-contextmenu` | `(column, event)` | Emitted on header right-click |
| `sort-change` | `({ column, prop, order })` | Emitted on sort change |
| `filter-change` | `(filters)` | Emitted on filter change |
| `current-change` | `(currentRow, oldRow)` | Emitted when current row changes |
| `expand-change` | `(row, expandedRows)` | Emitted on row expand/collapse |
| `page-change` | `(page)` | Emitted on page change |
| `page-limit-change` | `(limit)` | Emitted on page limit change |

### Methods

| Method | Parameters | Description |
|--------|------------|-------------|
| `clearSelection()` | - | Clear all selections |
| `toggleRowSelection(row, selected)` | `row, selected?` | Toggle row selection |
| `toggleAllSelection()` | - | Toggle all selection |
| `toggleRowExpansion(row, expanded)` | `row, expanded?` | Toggle row expansion |
| `setCurrentRow(row)` | `row` | Set current row |
| `clearSort()` | - | Clear sorting |
| `clearFilter(columnKeys)` | `columnKeys?` | Clear filters |
| `doLayout()` | - | Recalculate layout |
| `sort(prop, order)` | `prop, order` | Manual sort |

### Slots

| Slot | Description |
|------|-------------|
| `default` | Table columns (`bk-table-column`) |
| `empty` | Custom empty state |
| `append` | Content appended to table body |

### Examples

```vue
<bk-table :data="tableData" border stripe>
  <bk-table-column type="selection" width="60" />
  <bk-table-column prop="name" label="Name" sortable />
  <bk-table-column prop="age" label="Age" width="100" />
  <bk-table-column prop="status" label="Status">
    <template slot-scope="{ row }">
      <bk-tag :theme="row.status === 'active' ? 'success' : 'danger'">
        {{ row.status }}
      </bk-tag>
    </template>
  </bk-table-column>
  <bk-table-column label="Actions" width="150">
    <template slot-scope="{ row }">
      <bk-button text theme="primary" @click="handleEdit(row)">Edit</bk-button>
      <bk-button text theme="danger" @click="handleDelete(row)">Delete</bk-button>
    </template>
  </bk-table-column>
</bk-table>
```

---

## TableColumn (bk-table-column)

Table column configuration.

### Props

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `type` | String | - | Column type: `'selection'` \| `'index'` \| `'expand'` |
| `index` | Number \| Function | - | Custom index (for type="index") |
| `columnKey` | String | - | Column key for filter |
| `label` | String | - | Column header text |
| `prop` | String | - | Data field name |
| `width` | String \| Number | - | Column width |
| `minWidth` | String \| Number | - | Minimum column width |
| `fixed` | String \| Boolean | - | Fixed column: `true` \| `'left'` \| `'right'` |
| `renderHeader` | Function | - | Custom header render function |
| `sortable` | Boolean \| String | `false` | Enable sorting (`true` \| `'custom'`) |
| `sortMethod` | Function | - | Custom sort method |
| `sortBy` | String \| Array \| Function | - | Sort by field |
| `sortOrders` | Array | `['ascending', 'descending', null]` | Sort order cycle |
| `resizable` | Boolean | `true` | Allow column resize |
| `formatter` | Function | - | Cell value formatter |
| `showOverflowTooltip` | Boolean | `false` | Tooltip on overflow |
| `align` | String | `'left'` | Alignment: `'left'` \| `'center'` \| `'right'` |
| `headerAlign` | String | - | Header alignment |
| `className` | String | - | Column class |
| `labelClassName` | String | - | Header class |
| `selectable` | Function | - | Row selectable condition |
| `reserveSelection` | Boolean | `false` | Reserve selection on data change |
| `filters` | Array | - | Filter options `[{ text, value }]` |
| `filterPlacement` | String | - | Filter dropdown placement |
| `filterMultiple` | Boolean | `true` | Allow multiple filters |
| `filterMethod` | Function | - | Custom filter method |
| `filteredValue` | Array | - | Filtered values |
| `asyncRenderHtml` | Boolean | `false` | Async render as HTML |

### Scoped Slot

```vue
<bk-table-column prop="name" label="Name">
  <template slot-scope="{ row, column, $index }">
    <!-- Custom cell content -->
    {{ row.name }}
  </template>
</bk-table-column>

<!-- Header slot -->
<bk-table-column prop="name">
  <template slot="header" slot-scope="{ column, $index }">
    Custom Header
  </template>
  <template slot-scope="{ row }">
    {{ row.name }}
  </template>
</bk-table-column>
```

---

## Pagination (bk-pagination)

Pagination component with page navigation and size control.

### Props

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `current` | Number | `1` | Current page (supports .sync) |
| `count` | Number | `0` | Total items |
| `limit` | Number | `10` | Items per page (supports .sync) |
| `limitList` | Array | `[10, 20, 50, 100]` | Page size options |
| `showLimit` | Boolean | `true` | Show page size selector |
| `showTotalCount` | Boolean | `true` | Show total count |
| `location` | String | `'right'` | Position: `'left'` \| `'right'` |
| `align` | String | `'left'` | Alignment: `'left'` \| `'center'` \| `'right'` |
| `type` | String | `'default'` | Type: `'default'` \| `'compact'` |
| `size` | String | `'default'` | Size: `'default'` \| `'small'` |
| `small` | Boolean | `false` | Small size (deprecated, use size) |
| `popoverOptions` | Object | `{}` | Popover config |
| `extCls` | String | `''` | External CSS class |
| `prevText` | String | - | Previous button text |
| `nextText` | String | - | Next button text |
| `beforeChange` | Function | - | Pre-change validation |

### Events

| Event | Parameters | Description |
|-------|------------|-------------|
| `change` | `(page)` | Emitted on page change |
| `limit-change` | `(limit)` | Emitted on limit change |
| `update:current` | `(page)` | For .sync modifier |
| `update:limit` | `(limit)` | For .sync modifier |

### Examples

```vue
<!-- Basic pagination -->
<bk-pagination
  :current.sync="pagination.current"
  :count="pagination.count"
  :limit.sync="pagination.limit"
  @change="handlePageChange"
  @limit-change="handleLimitChange"
/>

<!-- Compact type -->
<bk-pagination
  :current.sync="page"
  :count="total"
  type="compact"
/>

<!-- Custom options -->
<bk-pagination
  :current.sync="page"
  :count="total"
  :limit-list="[5, 10, 20, 50]"
/>
```

---

## Tree (bk-tree)

Tree structure component with expand, selection, and drag support.

### Props

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `data` | Array | `[]` | Tree data |
| `nodeKey` | String | - | Unique node key field |
| `showIcon` | Boolean | `true` | Show node icons |
| `showCheckbox` | Boolean | `false` | Show checkboxes |
| `selectable` | Boolean | `true` | Enable node selection |
| `multiple` | Boolean | `false` | Multiple node selection |
| `emptyText` | String | `'暂无数据'` | Empty state text |
| `defaultExpandAll` | Boolean | `false` | Expand all by default |
| `defaultExpandedKeys` | Array | - | Initially expanded node keys |
| `defaultCheckedKeys` | Array | - | Initially checked node keys |
| `autoCheckChildren` | Boolean | `true` | Auto check children nodes |
| `expandOnClickNode` | Boolean | `true` | Expand on node click |
| `checkOnClickNode` | Boolean | `false` | Check on node click |
| `highlightCurrent` | Boolean | `false` | Highlight current node |
| `filterMethod` | Function | - | Custom filter method |
| `accordion` | Boolean | `false` | Accordion mode (single expand) |
| `indent` | Number | `18` | Indent width (px) |
| `iconOpen` | String | `'icon-folder-open'` | Open folder icon |
| `iconClose` | String | `'icon-folder'` | Closed folder icon |
| `iconDocument` | String | `'icon-file'` | Leaf node icon |
| `draggable` | Boolean | `false` | Enable drag & drop |
| `allowDrag` | Function | - | Allow drag condition |
| `allowDrop` | Function | - | Allow drop condition |
| `lazy` | Boolean | `false` | Lazy load children |
| `load` | Function | - | Lazy load function |
| `props` | Object | - | Field mapping `{ label, children, isLeaf }` |
| `extCls` | String | `''` | External CSS class |

### Events

| Event | Parameters | Description |
|-------|------------|-------------|
| `node-click` | `(node, data, event)` | Emitted on node click |
| `node-contextmenu` | `(event, data, node)` | Emitted on right-click |
| `node-expand` | `(data, node)` | Emitted on node expand |
| `node-collapse` | `(data, node)` | Emitted on node collapse |
| `check` | `(data, { checkedNodes, checkedKeys, halfCheckedNodes, halfCheckedKeys })` | Emitted on check |
| `check-change` | `(data, checked, indeterminate)` | Emitted when check state changes |
| `current-change` | `(data, node)` | Emitted when current node changes |
| `node-drag-start` | `(node, event)` | Emitted when drag starts |
| `node-drag-enter` | `(draggingNode, dropNode, event)` | Emitted when drag enters |
| `node-drag-leave` | `(draggingNode, dropNode, event)` | Emitted when drag leaves |
| `node-drag-over` | `(draggingNode, dropNode, event)` | Emitted when dragging over |
| `node-drag-end` | `(draggingNode, dropNode, dropType, event)` | Emitted when drag ends |
| `node-drop` | `(draggingNode, dropNode, dropType, event)` | Emitted after drop |

### Methods

| Method | Parameters | Returns | Description |
|--------|------------|---------|-------------|
| `filter(keyword)` | `keyword` | - | Filter nodes |
| `getNode(data)` | `data \| key` | `Node` | Get node by data or key |
| `getCheckedKeys(leafOnly)` | `leafOnly?` | `Array` | Get checked keys |
| `getCheckedNodes(leafOnly)` | `leafOnly?` | `Array` | Get checked nodes |
| `setCheckedKeys(keys, leafOnly)` | `keys, leafOnly?` | - | Set checked keys |
| `setCheckedNodes(nodes)` | `nodes` | - | Set checked nodes |
| `getHalfCheckedKeys()` | - | `Array` | Get half-checked keys |
| `getHalfCheckedNodes()` | - | `Array` | Get half-checked nodes |
| `getCurrentKey()` | - | `Any` | Get current node key |
| `getCurrentNode()` | - | `Object` | Get current node data |
| `setCurrentKey(key)` | `key` | - | Set current node by key |
| `setCurrentNode(node)` | `node` | - | Set current node |
| `append(data, parentNode)` | `data, parentNode?` | - | Append child node |
| `insertBefore(data, refNode)` | `data, refNode` | - | Insert before node |
| `insertAfter(data, refNode)` | `data, refNode` | - | Insert after node |
| `remove(data)` | `data \| node` | - | Remove node |
| `updateKeyChildren(key, data)` | `key, data` | - | Update node children |

### Scoped Slot

```vue
<bk-tree :data="treeData" node-key="id">
  <template slot-scope="{ node, data }">
    <span class="custom-tree-node">
      <span>{{ data.name }}</span>
      <span>
        <bk-button text size="small" @click="handleEdit(data)">Edit</bk-button>
        <bk-button text size="small" @click="handleDelete(node, data)">Delete</bk-button>
      </span>
    </span>
  </template>
</bk-tree>
```

### Examples

```vue
<!-- Basic tree -->
<bk-tree :data="treeData" node-key="id" />

<!-- With checkbox -->
<bk-tree
  :data="treeData"
  node-key="id"
  show-checkbox
  :default-checked-keys="['1', '2']"
/>

<!-- Lazy load -->
<bk-tree
  :data="treeData"
  node-key="id"
  lazy
  :load="loadChildren"
/>

<script>
methods: {
  loadChildren(node, resolve) {
    if (node.level === 0) {
      return resolve([{ id: '1', name: 'Root' }])
    }
    fetchChildren(node.data.id).then(children => {
      resolve(children)
    })
  }
}
</script>

<!-- With filtering -->
<bk-input v-model="filterText" placeholder="Filter" />
<bk-tree ref="tree" :data="treeData" :filter-method="filterNode" />

<script>
watch: {
  filterText(val) {
    this.$refs.tree.filter(val)
  }
},
methods: {
  filterNode(value, data) {
    if (!value) return true
    return data.name.indexOf(value) !== -1
  }
}
</script>
```

---

## BigTree (bk-big-tree)

Optimized tree for large datasets using virtual scrolling.

### Props

Same as `bk-tree`, plus:

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `height` | Number | `300` | Container height |
| `nodeHeight` | Number | `32` | Node row height |
| `useDefaultEmpty` | Boolean | `false` | Use default empty state |

### Usage

```vue
<bk-big-tree
  :data="largeTreeData"
  node-key="id"
  :height="400"
  :node-height="32"
/>
```

---

## Collapse (bk-collapse)

Collapsible panel component.

### Props

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `value` / `v-model` | Array \| String | - | Active panel name(s) |
| `accordion` | Boolean | `false` | Accordion mode (single open) |
| `extCls` | String | `''` | External CSS class |

### Events

| Event | Parameters | Description |
|-------|------------|-------------|
| `input` | `(activeNames)` | Emitted on change (for v-model) |
| `item-click` | `(name)` | Emitted when panel clicked |

### Slots

| Slot | Description |
|------|-------------|
| `default` | Collapse items (`bk-collapse-item`) |

---

## CollapseItem (bk-collapse-item)

Collapse panel item.

### Props

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `name` | String \| Number | - | Panel identifier |
| `title` | String | - | Panel header title |
| `disabled` | Boolean | `false` | Disable panel |
| `hideArrow` | Boolean | `false` | Hide expand arrow |
| `contentHiddenType` | String | `'hidden'` | Hidden type: `'hidden'` \| `'none'` |
| `extCls` | String | `''` | External CSS class |

### Slots

| Slot | Description |
|------|-------------|
| `default` | Panel content |
| `title` | Custom header |

### Examples

```vue
<bk-collapse v-model="activeNames">
  <bk-collapse-item name="1" title="Panel 1">
    Content 1
  </bk-collapse-item>
  <bk-collapse-item name="2" title="Panel 2">
    Content 2
  </bk-collapse-item>
  <bk-collapse-item name="3" title="Panel 3" disabled>
    Content 3 (disabled)
  </bk-collapse-item>
</bk-collapse>

<!-- Accordion mode -->
<bk-collapse v-model="activeName" accordion>
  ...
</bk-collapse>
```

---

## Card (bk-card)

Card container component.

### Props

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `title` | String | `''` | Card title |
| `showHead` | Boolean | `true` | Show card header |
| `showFoot` | Boolean | `false` | Show card footer |
| `isEdit` | Boolean | `false` | Enable title editing |
| `isCollapse` | Boolean | `false` | Enable collapse |
| `collapseStatus` | Boolean | `true` | Collapse state (supports .sync) |
| `collapseIcons` | Array | `['icon-angle-right', 'icon-angle-down']` | Collapse icons |
| `position` | String | `'left'` | Collapse icon position |
| `border` | Boolean | `true` | Show border |
| `disableHeaderStyle` | Boolean | `false` | Disable header style |
| `hoverable` | Boolean | `false` | Enable hover effect |

### Events

| Event | Parameters | Description |
|-------|------------|-------------|
| `edit` | `(title: String)` | Emitted when title edited |
| `update:collapseStatus` | `(status: Boolean)` | Emitted on collapse change |

### Slots

| Slot | Description |
|------|-------------|
| `header` | Custom header |
| `default` | Card body content |
| `footer` | Card footer content |

### Examples

```vue
<bk-card title="Card Title">
  Card content goes here
</bk-card>

<!-- With footer -->
<bk-card title="Card Title" :show-foot="true">
  Card content
  <template slot="footer">
    <bk-button theme="primary">Save</bk-button>
  </template>
</bk-card>

<!-- Collapsible -->
<bk-card title="Collapsible Card" :is-collapse="true" :collapse-status.sync="collapsed">
  Collapsible content
</bk-card>
```

---

## Description (bk-description)

Description list for key-value displays.

### Props

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `column` | Number \| String | `1` | Number of columns |
| `labelAlign` | String | `'left'` | Label alignment: `'left'` \| `'center'` \| `'right'` |
| `labelWidth` | Number \| String | - | Label width |
| `colon` | Boolean | `true` | Show colon after label |
| `isAlign` | Boolean | - | Strict column alignment |
| `extCls` | String | `''` | External CSS class |
| `contentCls` | String | `''` | Content cell class |
| `contentStyle` | String | `''` | Content cell style |
| `labelCls` | String | `''` | Label cell class |
| `labelStyle` | String | `''` | Label cell style |

### Examples

```vue
<bk-description :column="2" label-width="100">
  <bk-description-item label="Name">John Doe</bk-description-item>
  <bk-description-item label="Email">john@example.com</bk-description-item>
  <bk-description-item label="Address" :span="2">
    123 Main Street, City, Country
  </bk-description-item>
</bk-description>
```

---

## DescriptionItem (bk-description-item)

Description list item.

### Props

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `label` | String | `''` | Label text |
| `span` | Number | `1` | Column span |
| `showOverflowTooltip` | Boolean \| Object | `false` | Tooltip on overflow |
| `lineClamp` | Number \| String | `1` | Max lines |
| `contentCls` | String | `''` | Content class |
| `contentStyle` | String | `''` | Content style |
| `labelCls` | String | `''` | Label class |
| `labelStyle` | String | `''` | Label style |

---

## Progress (bk-progress)

Linear progress bar.

### Props

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `percent` | Number | `0` | Progress value (0-1) |
| `theme` | String | `'primary'` | Theme: `'primary'` \| `'warning'` \| `'success'` \| `'danger'` |
| `size` | String | `'normal'` | Size: `'small'` \| `'normal'` \| `'large'` |
| `strokeWidth` | Number | - | Bar height (px) |
| `textInside` | Boolean | `false` | Show text inside bar |
| `showText` | Boolean | `true` | Show percentage text |
| `color` | String | `''` | Custom progress color |
| `titleStyle` | Object | `{ fontSize: '16px' }` | Text style |
| `fixed` | Number | `0` | Decimal places (0-20) |
| `extCls` | String | `''` | External CSS class |

### Slots

| Slot | Description |
|------|-------------|
| `default` | Custom text content |

### Examples

```vue
<bk-progress :percent="0.5" />
<bk-progress :percent="0.75" theme="success" />
<bk-progress :percent="0.3" text-inside :stroke-width="18" />
```

---

## RoundProgress (bk-round-progress)

Circular progress indicator.

### Props

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `percent` | Number | `0` | Progress value (0-1) |
| `width` | String | - | Circle diameter |
| `config` | Object | - | Configuration object |
| `title` | String | - | Title text below |
| `content` | String \| Number | - | Custom center content |
| `numShow` | Boolean | `true` | Show center number |
| `numUnit` | String | `'%'` | Number unit |
| `numStyle` | Object | `{ fontSize: '16px' }` | Number style |
| `titleStyle` | Object | `{ fontSize: '16px' }` | Title style |
| `extCls` | String | `''` | External CSS class |

### Config Object

```javascript
config: {
  strokeWidth: 5,      // Ring thickness
  bgColor: 'gray',     // Background color
  activeColor: 'green' // Progress color
}
```

### Examples

```vue
<bk-round-progress :percent="0.75" width="100px" />

<bk-round-progress
  :percent="0.5"
  width="120px"
  :config="{ strokeWidth: 8, activeColor: '#3a84ff' }"
  title="Download"
/>
```

---

## Timeline (bk-timeline)

Timeline component for event sequences.

### Props

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `list` | Array | **required** | Timeline items |
| `titleAble` | Boolean | `false` | Enable title attribute |
| `extCls` | String | `''` | External CSS class |

### List Item Structure

```javascript
{
  tag: 'Title',              // Item title
  content: 'Description',    // Item content (String or VNode)
  description: 'Time',       // Additional description
  icon: 'icon-class',        // Custom icon (String or VNode)
  color: 'blue',             // Dot color: 'blue' | 'red' | 'green' | 'yellow' | 'gray'
  type: 'primary',           // Type: 'default' | 'primary' | 'warning' | 'success' | 'danger'
  size: 'normal'             // Dot size
}
```

### Events

| Event | Parameters | Description |
|-------|------------|-------------|
| `select` | `(item)` | Emitted when item clicked |

### Slots

| Slot | Description |
|------|-------------|
| `title{index}` | Custom title for item at index |
| `nodeContent{index}` | Custom content for item at index |

### Examples

```vue
<bk-timeline :list="timelineData" />

<script>
data() {
  return {
    timelineData: [
      { tag: 'Step 1', content: 'Created', color: 'green' },
      { tag: 'Step 2', content: 'Processing', color: 'blue' },
      { tag: 'Step 3', content: 'Completed', color: 'green', type: 'success' }
    ]
  }
}
</script>
```

---

## VirtualScroll (bk-virtual-scroll)

Virtual scrolling container for large lists.

### Props

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `list` | Array | `[]` | Data list |
| `itemHeight` | Number | `30` | Item height (px) |
| `groupItemCount` | Number | `20` | Items per group |
| `showIndex` | Boolean | `true` | Show item index |
| `minWidth` | Number | - | Minimum width |
| `height` | Number | - | Container height |
| `scrollXHidden` | Boolean | `false` | Hide horizontal scroll |
| `scrollYHidden` | Boolean | `false` | Hide vertical scroll |
| `extCls` | String | `''` | External CSS class |

### Events

| Event | Parameters | Description |
|-------|------------|-------------|
| `change` | `({ startIndex, endIndex })` | Emitted on visible range change |

### Scoped Slot

```vue
<bk-virtual-scroll :list="largeList" :item-height="40" :height="400">
  <template slot-scope="{ data }">
    <div class="list-item">{{ data.name }}</div>
  </template>
</bk-virtual-scroll>
```

---

## Image (bk-image)

Image component with lazy loading and preview.

### Props

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `src` | String | - | Image source URL |
| `fallback` | String | - | Fallback image on error |
| `fit` | String | - | Object-fit: `'none'` \| `'contain'` \| `'cover'` \| `'fill'` \| `'scale-down'` |
| `lazy` | Boolean | - | Enable lazy loading |
| `scrollContainer` | Object | `{}` | Scroll container for lazy load |
| `previewSrcList` | Array | `[]` | Images for preview mode |
| `isShowPreviewTitle` | Boolean | `true` | Show title in preview |
| `zIndex` | Number | `2000` | Preview z-index |

### Events

| Event | Parameters | Description |
|-------|------------|-------------|
| `error` | `(event)` | Emitted on load error |

### Slots

| Slot | Description |
|------|-------------|
| `placeholder` | Loading placeholder |
| `error` | Error content |

### Examples

```vue
<!-- Basic -->
<bk-image src="/path/to/image.jpg" />

<!-- With preview -->
<bk-image
  src="/thumbnail.jpg"
  :preview-src-list="['/full1.jpg', '/full2.jpg']"
/>

<!-- Lazy load -->
<bk-image src="/image.jpg" lazy />
```

---

## AnimateNumber (bk-animate-number)

Animated number counter.

### Props

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `value` | Number | **required** | Target number |
| `useThousand` | Boolean | `false` | Use thousand separator |
| `digits` | Number | `0` | Decimal places |
| `extCls` | String | `''` | External CSS class |

### Examples

```vue
<bk-animate-number :value="12345" use-thousand />
<bk-animate-number :value="99.9" :digits="1" />
```

---

## Transfer (bk-transfer)

Transfer list component for moving items between two lists.

### Props

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `sourceList` | Array | `[]` | Source list data |
| `displayKey` | String | `'name'` | Display field key |
| `settingKey` | String | `'id'` | Value field key |
| `sortKey` | String | - | Sort field key |
| `sortable` | Boolean | `false` | Enable sorting |
| `targetList` | Array | `[]` | Initial target values (v-model) |
| `title` | Array | `['Source', 'Target']` | Panel titles |
| `emptyContent` | Array | `['No Data', 'No Data']` | Empty state text |
| `showOverflowTips` | Boolean | `false` | Show tooltip on overflow |
| `searchable` | Boolean | `false` | Enable search |
| `searchPlaceholder` | String | - | Search placeholder |
| `extCls` | String | `''` | External CSS class |

### Events

| Event | Parameters | Description |
|-------|------------|-------------|
| `change` | `(sourceList, targetList, targetValues)` | Emitted when transfer changes |

### Examples

```vue
<bk-transfer
  :source-list="allItems"
  :target-list.sync="selectedItems"
  :title="['Available', 'Selected']"
  searchable
/>
```
