# Feedback Components

## Dialog (bk-dialog)

Modal dialog component.

### Props

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `value` / `v-model` | Boolean | `false` | Dialog visibility |
| `title` | String | `''` | Dialog title |
| `width` | Number \| String | `400` | Dialog width |
| `headerPosition` | String | `'left'` | Header alignment: `'left'` \| `'center'` |
| `closeIcon` | Boolean | `true` | Show close icon |
| `showFooter` | Boolean | `true` | Show footer |
| `showMask` | Boolean | `true` | Show backdrop |
| `maskClose` | Boolean | `true` | Close on backdrop click |
| `escClose` | Boolean | `true` | Close on ESC key |
| `fullscreen` | Boolean | `false` | Fullscreen mode |
| `draggable` | Boolean | `true` | Enable drag |
| `scrollable` | Boolean | `false` | Enable body scroll when open |
| `okText` | String | `'确定'` | Confirm button text |
| `cancelText` | String | `'取消'` | Cancel button text |
| `confirmFn` | Function | - | Async confirm handler (return true to close) |
| `cancelFn` | Function | - | Cancel handler |
| `beforeClose` | Function | - | Before close hook |
| `confirmLoading` | Boolean | `false` | Show confirm loading state |
| `autoClose` | Boolean | `true` | Auto close after confirm |
| `theme` | String | `'primary'` | Confirm button theme |
| `position` | Object | - | Custom position `{ top, left }` |
| `transfer` | Boolean | `true` | Transfer to body |
| `zIndex` | Number | - | Custom z-index |
| `extCls` | String | `''` | External CSS class |

### Events

| Event | Parameters | Description |
|-------|------------|-------------|
| `input` | `(visible: Boolean)` | Emitted on visibility change (for v-model) |
| `confirm` | - | Emitted when confirmed (without confirmFn) |
| `cancel` | - | Emitted when cancelled |
| `after-leave` | - | Emitted after dialog closed animation |
| `value-change` | `(visible: Boolean)` | Emitted on visibility change |

### Slots

| Slot | Description |
|------|-------------|
| `default` | Dialog body content |
| `header` | Custom header |
| `footer` | Custom footer |
| `tools` | Custom tools area (top right) |

### Examples

```vue
<!-- Basic dialog -->
<bk-button @click="showDialog = true">Open Dialog</bk-button>
<bk-dialog v-model="showDialog" title="Dialog Title">
  Dialog content
</bk-dialog>

<!-- With async confirm -->
<bk-dialog
  v-model="showDialog"
  title="Confirm Action"
  :confirm-fn="handleConfirm"
>
  Are you sure you want to proceed?
</bk-dialog>

<script>
methods: {
  async handleConfirm() {
    await this.doSomething()
    return true // Return true to close
  }
}
</script>

<!-- Custom footer -->
<bk-dialog v-model="showDialog" title="Custom Footer" :show-footer="false">
  <template slot="footer">
    <bk-button @click="showDialog = false">Cancel</bk-button>
    <bk-button theme="primary" :loading="loading" @click="submit">
      Submit
    </bk-button>
  </template>
</bk-dialog>

<!-- Fullscreen -->
<bk-dialog v-model="showDialog" title="Fullscreen" fullscreen>
  Full screen content
</bk-dialog>
```

---

## Sideslider (bk-sideslider)

Side panel slider component.

### Props

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `isShow` | Boolean | `false` | Panel visibility (supports .sync) |
| `title` | String | `''` | Panel title |
| `width` | Number | `400` | Panel width |
| `direction` | String | `'right'` | Slide direction: `'left'` \| `'right'` |
| `quickClose` | Boolean | `true` | Close on backdrop click |
| `showMask` | Boolean | `true` | Show backdrop |
| `transfer` | Boolean | `false` | Transfer to body |
| `beforeClose` | Function | - | Before close hook (return false to prevent) |
| `zIndex` | Number | - | Custom z-index |
| `extCls` | String | `''` | External CSS class |

### Events

| Event | Parameters | Description |
|-------|------------|-------------|
| `update:isShow` | `(visible: Boolean)` | Emitted for .sync modifier |
| `shown` | - | Emitted after panel shown |
| `hidden` | - | Emitted after panel hidden |
| `animation-end` | - | Emitted after animation completes |

### Slots

| Slot | Description |
|------|-------------|
| `header` | Custom header |
| `content` | Panel content |
| `footer` | Panel footer |

### Examples

```vue
<bk-button @click="showSlider = true">Open Slider</bk-button>

<bk-sideslider :is-show.sync="showSlider" title="Panel Title" :width="600">
  <template slot="content">
    <div class="slider-content">
      Slider content here
    </div>
  </template>
  <template slot="footer">
    <bk-button @click="showSlider = false">Cancel</bk-button>
    <bk-button theme="primary" @click="handleSave">Save</bk-button>
  </template>
</bk-sideslider>

<!-- Left direction -->
<bk-sideslider :is-show.sync="showSlider" direction="left">
  ...
</bk-sideslider>
```

---

## Message (bk-message)

Global message notification.

### Programmatic API

```javascript
this.$bkMessage(options)
// or
this.$bkMessage({ message: 'Hello', theme: 'success' })
```

### Options

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `message` | String \| VNode | - | Message content |
| `theme` | String | `'primary'` | Theme: `'primary'` \| `'error'` \| `'warning'` \| `'success'` |
| `delay` | Number | `3000` | Auto close delay (ms), 0 = no auto close |
| `dismissable` | Boolean | `true` | Show close button |
| `offsetY` | Number | `30` | Vertical offset (px) |
| `spacing` | Number | `10` | Spacing between messages |
| `limit` | Number | `0` | Max messages (0 = no limit) |
| `ellipsisLine` | Number | `1` | Max lines before ellipsis |
| `ellipsisCopy` | Boolean | `false` | Enable copy on ellipsis |
| `onClose` | Function | - | Close callback |
| `extCls` | String | `''` | External CSS class |

### Static Methods

```javascript
// Shorthand methods
this.$bkMessage.primary('Primary message')
this.$bkMessage.success('Success message')
this.$bkMessage.warning('Warning message')
this.$bkMessage.error('Error message')

// Close all messages
this.$bkMessage.close()
```

### Examples

```javascript
// Basic usage
this.$bkMessage({ message: 'Operation completed', theme: 'success' })

// With callback
this.$bkMessage({
  message: 'File uploaded',
  theme: 'success',
  delay: 5000,
  onClose: () => {
    console.log('Message closed')
  }
})

// Error message
this.$bkMessage({
  message: 'Operation failed',
  theme: 'error',
  delay: 0  // Don't auto close
})

// With limit
this.$bkMessage({
  message: 'New notification',
  limit: 3  // Max 3 messages at a time
})
```

---

## Notify (bk-notify)

Notification component with positioning support.

### Programmatic API

```javascript
this.$bkNotify(options)
```

### Options

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `title` | String | `''` | Notification title |
| `message` | String | `''` | Notification content |
| `theme` | String | `'primary'` | Theme: `'primary'` \| `'error'` \| `'warning'` \| `'success'` |
| `position` | String | `'top-right'` | Position: `'top-right'` \| `'top-left'` \| `'bottom-right'` \| `'bottom-left'` |
| `delay` | Number | `5000` | Auto close delay (ms), 0 = no auto close |
| `dismissable` | Boolean | `true` | Show close button |
| `limit` | Number | `0` | Max notifications |
| `limitLine` | Number | `2` | Max content lines |
| `showViewMore` | Boolean | `false` | Show "view more" button |
| `offsetX` | Number | `10` | Horizontal offset |
| `offsetY` | Number | `30` | Vertical offset |
| `spacing` | Number | `10` | Spacing between notifications |
| `icon` | String | `''` | Custom icon class |
| `useHTMLString` | Boolean | `false` | Render as HTML (XSS risk) |
| `onClose` | Function | - | Close callback |
| `extCls` | String | `''` | External CSS class |

### Static Methods

```javascript
// Close specific notification
this.$bkNotify.close(id, callback)

// Close all notifications
this.$bkNotify.close()
```

### Examples

```javascript
// Basic notification
this.$bkNotify({
  title: 'Success',
  message: 'File uploaded successfully',
  theme: 'success'
})

// Error notification
this.$bkNotify({
  title: 'Error',
  message: 'Failed to save changes',
  theme: 'error',
  delay: 0  // Don't auto close
})

// Bottom position
this.$bkNotify({
  title: 'Info',
  message: 'New message received',
  position: 'bottom-right'
})
```

---

## InfoBox (bk-info-box)

Confirmation dialog box.

### Programmatic API

```javascript
this.$bkInfo(options)
```

### Options

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `title` | String | `''` | Title text |
| `subTitle` | String | `''` | Subtitle/description text |
| `type` | String | `'primary'` | Type: `'primary'` \| `'success'` \| `'warning'` \| `'error'` \| `'loading'` |
| `confirmText` | String | `'确认'` | Confirm button text |
| `cancelText` | String | `'取消'` | Cancel button text |
| `showFooter` | Boolean | `true` | Show footer buttons |
| `confirmFn` | Function | - | Async confirm callback |
| `cancelFn` | Function | - | Cancel callback |
| `closeFn` | Function | - | Close callback |
| `closeIcon` | Boolean | `true` | Show close icon |
| `escClose` | Boolean | `true` | Close on ESC |
| `maskClose` | Boolean | `true` | Close on backdrop click |
| `width` | Number \| String | `400` | Dialog width |
| `zIndex` | Number | - | Custom z-index |
| `extCls` | String | `''` | External CSS class |

### Returns

Returns a Promise that resolves on confirm, rejects on cancel.

### Examples

```javascript
// Basic confirmation
this.$bkInfo({
  title: 'Confirm Delete',
  subTitle: 'Are you sure you want to delete this item?',
  confirmFn: async () => {
    await this.deleteItem()
  }
})

// Using Promise
try {
  await this.$bkInfo({
    title: 'Confirm',
    subTitle: 'Continue?'
  })
  // User confirmed
} catch (e) {
  // User cancelled
}

// Warning type
this.$bkInfo({
  title: 'Warning',
  subTitle: 'This action cannot be undone',
  type: 'warning',
  confirmFn: () => {
    // Handle confirm
  }
})

// Loading type (no buttons)
const loading = this.$bkInfo({
  title: 'Loading',
  subTitle: 'Please wait...',
  type: 'loading',
  showFooter: false,
  maskClose: false
})
// Later: loading.close()
```

---

## Loading (bk-loading)

Loading overlay component.

### Programmatic API

```javascript
const loading = this.$bkLoading(options)
// Later: loading.hide()
```

### Options

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `title` | String | `''` | Loading text |
| `target` | Element \| String | - | Target element or selector |
| `opacity` | Number | `0.9` | Overlay opacity |
| `color` | String | - | Loading color |
| `zIndex` | Number | - | Custom z-index |
| `size` | String | `'normal'` | Size: `'small'` \| `'normal'` \| `'large'` |
| `mode` | String | `'default'` | Mode: `'default'` \| `'spin'` |
| `delay` | Number | `0` | Delay before showing (ms) |
| `extCls` | String | `''` | External CSS class |
| `afterLeave` | Function | - | Callback after hidden |

### Methods

```javascript
const loading = this.$bkLoading({ title: 'Loading...' })

// Hide loading
loading.hide()
// or
this.$bkLoading.hide()
```

### Examples

```javascript
// Full page loading
const loading = this.$bkLoading({ title: 'Loading data...' })
await fetchData()
loading.hide()

// Target element loading
const loading = this.$bkLoading({
  title: 'Loading...',
  target: '.content-wrapper'
})

// Spin mode
const loading = this.$bkLoading({
  title: 'Processing...',
  mode: 'spin'
})
```

---

## Alert (bk-alert)

Alert banner component.

### Props

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `type` | String | `'primary'` | Type: `'primary'` \| `'error'` \| `'warning'` \| `'success'` \| `'info'` |
| `title` | String | `''` | Alert title |
| `subTitle` | String | `''` | Alert description |
| `closable` | Boolean | `false` | Show close button |
| `closeText` | String | - | Custom close button text |
| `showIcon` | Boolean | `true` | Show icon |
| `icon` | String | - | Custom icon class |
| `ellipsisLine` | Number | `0` | Max lines (0 = no limit) |
| `extCls` | String | `''` | External CSS class |

### Events

| Event | Parameters | Description |
|-------|------------|-------------|
| `close` | - | Emitted when closed |

### Slots

| Slot | Description |
|------|-------------|
| `title` | Custom title |
| `sub-title` | Custom description |
| `close-text` | Custom close button |

### Examples

```vue
<bk-alert type="info" title="Information" />

<bk-alert
  type="warning"
  title="Warning"
  sub-title="Please check your input"
  closable
/>

<bk-alert type="error" closable @close="handleClose">
  <template slot="title">Custom Error Title</template>
  <template slot="sub-title">
    Error details with <a href="#">link</a>
  </template>
</bk-alert>
```

---

## Exception (bk-exception)

Exception page component for error states.

### Props

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `type` | String \| Number | `404` | Type: `'404'` \| `'403'` \| `'500'` \| `'building'` \| `'empty'` \| `'search-empty'` \| `'login'` |
| `scene` | String | `'page'` | Scene: `'page'` \| `'part'` |
| `extCls` | String | `''` | External CSS class |

### Slots

| Slot | Description |
|------|-------------|
| `default` | Custom message content |

### Examples

```vue
<!-- 404 Page -->
<bk-exception type="404">
  <span>Page not found</span>
  <bk-button theme="primary" @click="goHome">Go Home</bk-button>
</bk-exception>

<!-- Empty state -->
<bk-exception type="empty" scene="part">
  No data available
</bk-exception>

<!-- Search empty -->
<bk-exception type="search-empty">
  No results found
</bk-exception>
```

---

## Popover (bk-popover)

Popover tooltip component (based on Tippy.js).

### Props

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `content` | String | `''` | Popover content |
| `placement` | String | `'top'` | Placement position |
| `theme` | String | `'dark'` | Theme: `'dark'` \| `'light'` |
| `trigger` | String | `'mouseenter focus'` | Trigger: `'mouseenter'` \| `'focus'` \| `'click'` \| `'manual'` |
| `interactive` | Boolean | `true` | Allow interaction |
| `arrow` | Boolean | `true` | Show arrow |
| `arrowType` | String | `'sharp'` | Arrow style |
| `delay` | Number | `100` | Show/hide delay |
| `distance` | Number | `10` | Distance from reference |
| `width` | String \| Number | `'auto'` | Popover width |
| `maxWidth` | String \| Number | `'auto'` | Max width |
| `height` | String \| Number | `'auto'` | Height |
| `maxHeight` | String \| Number | `'auto'` | Max height |
| `offset` | Number \| String | `0` | Offset |
| `always` | Boolean | `false` | Always visible |
| `followCursor` | Boolean | `false` | Follow mouse cursor |
| `sticky` | Boolean | `false` | Sticky positioning |
| `boundary` | String | `'window'` | Boundary element |
| `animation` | String | `'shift-away'` | Animation type |
| `onShow` | Function | - | Show callback |
| `onHide` | Function | - | Hide callback |
| `tippyOptions` | Object | `{}` | Additional Tippy options |
| `disabled` | Boolean | `false` | Disable popover |
| `zIndex` | Number \| String | - | Z-index |
| `extCls` | String | `''` | External CSS class |

### Events

| Event | Parameters | Description |
|-------|------------|-------------|
| `show` | - | Emitted when shown |
| `hide` | - | Emitted when hidden |

### Slots

| Slot | Description |
|------|-------------|
| `default` | Reference element |
| `content` | Popover content |

### Methods

| Method | Description |
|--------|-------------|
| `showHandler()` | Show popover |
| `hideHandler()` | Hide popover |

### Examples

```vue
<!-- Basic popover -->
<bk-popover content="Tooltip content">
  <bk-button>Hover me</bk-button>
</bk-popover>

<!-- Click trigger -->
<bk-popover trigger="click">
  <bk-button>Click me</bk-button>
  <template slot="content">
    <div class="popover-content">
      Popover content
    </div>
  </template>
</bk-popover>

<!-- Custom placement -->
<bk-popover content="Bottom tooltip" placement="bottom">
  <span>Hover for bottom tooltip</span>
</bk-popover>

<!-- Interactive content -->
<bk-popover trigger="click" theme="light" :width="300">
  <bk-button>Menu</bk-button>
  <template slot="content">
    <ul class="menu-list">
      <li @click="handleAction('edit')">Edit</li>
      <li @click="handleAction('delete')">Delete</li>
    </ul>
  </template>
</bk-popover>
```

---

## Popconfirm (bk-popconfirm)

Popover confirmation component.

### Props

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `title` | String | - | Confirmation title |
| `content` | String | - | Confirmation content |
| `trigger` | String | `'mouseenter focus'` | Trigger event |
| `theme` | String | `'none'` | Theme: `'primary'` \| `'warning'` \| `'success'` \| `'danger'` \| `'none'` |
| `confirmText` | String | `'确定'` | Confirm button text |
| `cancelText` | String | `'取消'` | Cancel button text |
| `confirmButtonIsText` | Boolean | `false` | Confirm as text button |
| `cancelButtonIsText` | Boolean | `false` | Cancel as text button |
| `disabled` | Boolean | `false` | Disable popconfirm |
| `width` | Number | `240` | Popover width |
| `beforeConfirm` | Function | - | Async validation (return true/false or Promise) |
| `useRingLoading` | Boolean | `false` | Use ring loading animation |
| `extPopoverCls` | String | `''` | Popover external class |

### Events

| Event | Parameters | Description |
|-------|------------|-------------|
| `confirm` | - | Emitted on confirm |
| `cancel` | - | Emitted on cancel |

### Slots

| Slot | Description |
|------|-------------|
| `default` | Reference element |
| `content` | Custom confirmation content |

### Examples

```vue
<bk-popconfirm
  title="Delete Confirmation"
  content="Are you sure you want to delete this item?"
  @confirm="handleDelete"
>
  <bk-button theme="danger">Delete</bk-button>
</bk-popconfirm>

<!-- With async validation -->
<bk-popconfirm
  title="Confirm Action"
  :before-confirm="validateAction"
  @confirm="handleConfirm"
>
  <bk-button>Confirm</bk-button>
</bk-popconfirm>

<script>
methods: {
  async validateAction() {
    // Return true to proceed, false to cancel
    return await this.checkCondition()
  }
}
</script>
```

---

## Spin (bk-spin)

Loading spinner component.

### Props

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `spinning` | Boolean | `true` | Whether animating |
| `theme` | String | `'primary'` | Theme: `'default'` \| `'primary'` \| `'warning'` \| `'error'` \| `'success'` \| `'danger'` \| `'info'` |
| `color` | String | `''` | Custom color |
| `size` | String | `'normal'` | Size: `'large'` \| `'normal'` \| `'small'` \| `'mini'` |
| `icon` | String | `''` | Custom bk-icon |
| `useRing` | Boolean | `false` | Use SVG ring animation |
| `placement` | String | `'bottom'` | Slot position: `'bottom'` \| `'right'` |
| `extCls` | String | `''` | External CSS class |

### Slots

| Slot | Description |
|------|-------------|
| `default` | Content next to spinner |

### Examples

```vue
<bk-spin />

<bk-spin size="large" theme="success" />

<bk-spin use-ring color="#3a84ff" />

<bk-spin>Loading data...</bk-spin>
```

---

## Affix (bk-affix)

Affix component that sticks to viewport.

### Props

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `offsetTop` | Number | `0` | Offset from top |
| `offsetBottom` | Number | - | Offset from bottom |
| `target` | String | `''` | Scroll container selector |
| `zIndex` | Number | `1000` | Z-index when fixed |
| `disabled` | Boolean | `false` | Disable affix |

### Events

| Event | Parameters | Description |
|-------|------------|-------------|
| `change` | `(isFixed: Boolean)` | Emitted when affix state changes |

### Methods

| Method | Description |
|--------|-------------|
| `updateStyle()` | Manually update styles |

### Examples

```vue
<bk-affix :offset-top="80">
  <bk-button>Sticky Button</bk-button>
</bk-affix>

<!-- Sticky to bottom -->
<bk-affix :offset-bottom="20">
  <div class="bottom-bar">Bottom Actions</div>
</bk-affix>
```

---

## BackTop (bk-back-top)

Back to top button component.

### Props

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `bottom` | Number | `40` | Distance from bottom |
| `right` | Number | `40` | Distance from right |
| `target` | String | `''` | Scroll container selector |
| `visibilityHeight` | Number | `200` | Scroll height before visible |

### Events

| Event | Parameters | Description |
|-------|------------|-------------|
| `click` | `(event)` | Emitted on click |

### Slots

| Slot | Description |
|------|-------------|
| `default` | Custom button content |

### Examples

```vue
<bk-back-top />

<!-- Custom position -->
<bk-back-top :bottom="60" :right="60" />

<!-- Custom content -->
<bk-back-top>
  <bk-button circle theme="primary" icon="icon-angle-up" />
</bk-back-top>
```

---

## ImageViewer (bk-image-viewer)

Image preview viewer.

### Props

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `urlList` | Array | `[]` | Image URL list |
| `zIndex` | Number | `2000` | Viewer z-index |
| `initialIndex` | Number | `0` | Initial image index |
| `isShowTitle` | Boolean | `true` | Show image title |
| `onSwitch` | Function | - | Switch callback |
| `onClose` | Function | - | Close callback |

### Events

| Event | Parameters | Description |
|-------|------------|-------------|
| `change` | `(index: Number)` | Emitted on image change |
| `hide` | - | Emitted when viewer closes |

### Keyboard Controls

- **ESC** - Close viewer
- **Space** - Toggle contain/original
- **Left Arrow** - Previous image
- **Right Arrow** - Next image
- **Up Arrow** - Zoom in
- **Down Arrow** - Zoom out

### Examples

```vue
<bk-image-viewer
  v-if="showViewer"
  :url-list="imageUrls"
  :initial-index="currentIndex"
  @hide="showViewer = false"
/>
```
