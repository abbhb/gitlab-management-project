# Navigation Components

## Navigation (bk-navigation)

Application navigation layout component with sidebar and header.

### Props

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `navWidth` | Number | `240` | Expanded sidebar width |
| `hoverWidth` | Number | `60` | Collapsed sidebar width |
| `sideTitle` | String | `''` | Sidebar title |
| `headerTitle` | String | `''` | Header title |
| `defaultOpen` | Boolean | `false` | Default expanded state |
| `hoverEnterDelay` | Number | `100` | Hover expand delay (ms) |
| `hoverLeaveDelay` | Number | `100` | Hover collapse delay (ms) |
| `navigationType` | String | `'left-right'` | Layout type: `'left-right'` \| `'top-bottom'` |
| `needMenu` | Boolean | `true` | Show menu |
| `headHeight` | Number | `52` | Header height |
| `themeColor` | String | `'#182132'` | Theme background color |
| `hoverTheme` | String | `'#182132'` | Hover background color |
| `sideHoverOpen` | Boolean | `true` | Enable hover expand |
| `extCls` | String | `''` | External CSS class |

### Events

| Event | Parameters | Description |
|-------|------------|-------------|
| `toggle` | `(isOpen: Boolean)` | Emitted when sidebar toggles |
| `toggle-click` | `(isOpen: Boolean)` | Emitted on toggle button click |
| `hover` | `(isHover: Boolean)` | Emitted on hover state change |

### Slots

| Slot | Description |
|------|-------------|
| `side-icon` | Sidebar logo icon |
| `header` | Header content |
| `menu` | Sidebar menu content |
| `default` | Main content area |
| `footer` | Footer content |
| `side-header` | Sidebar header (replaces side-icon + title) |

### Examples

```vue
<bk-navigation
  :nav-width="260"
  side-title="Application"
  :default-open="true"
>
  <template slot="side-icon">
    <img src="/logo.png" />
  </template>
  
  <template slot="header">
    <div class="header-content">
      <bk-input placeholder="Search..." />
      <bk-dropdown-menu>
        <template slot="dropdown-trigger">
          <span class="user-name">Admin</span>
        </template>
        <template slot="dropdown-content">
          <li @click="handleLogout">Logout</li>
        </template>
      </bk-dropdown-menu>
    </div>
  </template>
  
  <template slot="menu">
    <bk-navigation-menu
      :default-active="activeMenu"
      @select="handleMenuSelect"
    >
      <bk-navigation-menu-item id="home" icon="icon-home">
        Home
      </bk-navigation-menu-item>
      <bk-navigation-menu-group name="Management" icon="icon-cog">
        <bk-navigation-menu-item id="users">Users</bk-navigation-menu-item>
        <bk-navigation-menu-item id="roles">Roles</bk-navigation-menu-item>
      </bk-navigation-menu-group>
    </bk-navigation-menu>
  </template>
  
  <div class="main-content">
    <router-view />
  </div>
</bk-navigation>
```

---

## NavigationMenu (bk-navigation-menu)

Navigation menu component for sidebar.

### Props

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `defaultActive` | String | `''` | Default active item ID |
| `openedKeys` | Array | `[]` | Default expanded group keys |
| `uniqueOpen` | Boolean | `false` | Unique group expand (accordion) |
| `toggleActive` | Boolean | `false` | Toggle item active state |
| `beforeNavChange` | Function | - | Before navigation change hook |
| `extCls` | String | `''` | External CSS class |

### Events

| Event | Parameters | Description |
|-------|------------|-------------|
| `select` | `(id, item)` | Emitted when menu item selected |
| `open` | `(id)` | Emitted when group opened |
| `close` | `(id)` | Emitted when group closed |

### Slots

| Slot | Description |
|------|-------------|
| `default` | Menu items/groups |

---

## NavigationMenuItem (bk-navigation-menu-item)

Navigation menu item.

### Props

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `id` | String | **required** | Item identifier |
| `icon` | String | - | Icon class |
| `disabled` | Boolean | `false` | Disable item |
| `hasChild` | Boolean | `false` | Has children (for lazy load) |

### Slots

| Slot | Description |
|------|-------------|
| `default` | Item label |
| `child` | Child items (for nested menu) |

---

## NavigationMenuGroup (bk-navigation-menu-group)

Navigation menu group (submenu).

### Props

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `name` | String | - | Group name/title |
| `icon` | String | - | Icon class |
| `disabled` | Boolean | `false` | Disable group |

### Slots

| Slot | Description |
|------|-------------|
| `default` | Group items |

---

## Tab (bk-tab)

Tab navigation component.

### Props

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `active` | String \| Number | `''` | Active tab name (supports .sync) |
| `type` | String | `'border-card'` | Tab style: `'border-card'` \| `'card'` \| `'unborder-card'` |
| `tabPosition` | String | `'top'` | Position: `'top'` \| `'bottom'` \| `'left'` \| `'right'` |
| `scrollStep` | Number | `200` | Scroll step for overflow |
| `closable` | Boolean | `false` | Show close button on tabs |
| `addable` | Boolean | `false` | Show add button |
| `sortable` | Boolean | `false` | Enable drag sort |
| `sortType` | String | `'replace'` | Sort type: `'replace'` \| `'insert'` |
| `labelHeight` | Number | `50` | Tab label height |
| `showHeader` | Boolean | `true` | Show tab header |
| `validateActive` | Boolean | `true` | Validate active tab exists |
| `beforeToggle` | Function | - | Before toggle hook |
| `extCls` | String | `''` | External CSS class |

### Events

| Event | Parameters | Description |
|-------|------------|-------------|
| `update:active` | `(name)` | Emitted for .sync modifier |
| `tab-change` | `(name)` | Emitted when active tab changes |
| `add-panel` | - | Emitted when add button clicked |
| `close-panel` | `(name, index)` | Emitted when tab closed |
| `sort-change` | `(dragIndex, dropIndex)` | Emitted after drag sort |
| `drag-start` | `(name, index)` | Emitted when drag starts |
| `drag-end` | - | Emitted when drag ends |

### Slots

| Slot | Description |
|------|-------------|
| `default` | Tab panels (`bk-tab-panel`) |
| `add` | Custom add button |
| `extension` | Extension area in header |
| `setting` | Setting area in header |

### Examples

```vue
<bk-tab :active.sync="activeTab" type="card" closable addable @add-panel="handleAdd">
  <bk-tab-panel
    v-for="tab in tabs"
    :key="tab.name"
    :name="tab.name"
    :label="tab.label"
  >
    {{ tab.content }}
  </bk-tab-panel>
</bk-tab>

<!-- With custom label -->
<bk-tab :active.sync="activeTab">
  <bk-tab-panel name="home">
    <template slot="label">
      <i class="bk-icon icon-home"></i> Home
    </template>
    Home content
  </bk-tab-panel>
</bk-tab>

<!-- Left position -->
<bk-tab :active.sync="activeTab" tab-position="left">
  ...
</bk-tab>
```

---

## TabPanel (bk-tab-panel)

Tab panel content.

### Props

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `name` | String \| Number | **required** | Panel identifier |
| `label` | String | `''` | Tab label text |
| `disabled` | Boolean | `false` | Disable tab |
| `closable` | Boolean | - | Override parent closable |
| `visible` | Boolean | `true` | Show/hide tab |
| `sortable` | Boolean | - | Override parent sortable |
| `renderDirective` | String | `'show'` | Render directive: `'show'` \| `'if'` |

### Slots

| Slot | Description |
|------|-------------|
| `default` | Panel content |
| `label` | Custom tab label |

---

## Steps (bk-steps)

Steps navigation component.

### Props

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `steps` | Array | `[]` | Steps data |
| `curStep` | Number | `1` | Current step (1-based, supports .sync) |
| `direction` | String | `'horizontal'` | Direction: `'horizontal'` \| `'vertical'` |
| `theme` | String | `'primary'` | Theme: `'primary'` \| `'success'` \| `'warning'` \| `'danger'` |
| `size` | String | `''` | Size: `''` \| `'small'` |
| `status` | String | `''` | Current status: `''` \| `'error'` \| `'loading'` |
| `lineType` | String | `'solid'` | Line type: `'solid'` \| `'dashed'` |
| `controllable` | Boolean | `false` | Allow clicking to navigate |
| `beforeChange` | Function | - | Before change hook |
| `extCls` | String | `''` | External CSS class |

### Steps Data Structure

```javascript
steps: [
  { title: 'Step 1', icon: 'icon-check-1', description: 'Description' },
  { title: 'Step 2' },
  { title: 'Step 3' }
]
```

### Events

| Event | Parameters | Description |
|-------|------------|-------------|
| `update:curStep` | `(step: Number)` | Emitted for .sync modifier |
| `step-changed` | `(step: Number)` | Emitted when step changes |

### Slots

For each step at index `i`:
- `step-{i}` - Custom step content

### Examples

```vue
<bk-steps :steps="stepsData" :cur-step.sync="currentStep" />

<script>
data() {
  return {
    currentStep: 1,
    stepsData: [
      { title: 'Basic Info', icon: 'icon-info' },
      { title: 'Configuration' },
      { title: 'Review' },
      { title: 'Complete', icon: 'icon-check-1' }
    ]
  }
}
</script>

<!-- Vertical steps -->
<bk-steps :steps="stepsData" :cur-step="step" direction="vertical" />

<!-- Controllable -->
<bk-steps :steps="stepsData" :cur-step.sync="step" controllable />

<!-- With before change validation -->
<bk-steps
  :steps="stepsData"
  :cur-step.sync="step"
  controllable
  :before-change="validateStep"
/>

<script>
methods: {
  async validateStep(newStep) {
    if (newStep > this.step) {
      return await this.validateCurrentStep()
    }
    return true
  }
}
</script>
```

---

## Breadcrumb (bk-breadcrumb)

Breadcrumb navigation component.

### Props

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `separator` | String | `'>'` | Separator character |
| `separatorClass` | String | - | Separator icon class |
| `extCls` | String | `''` | External CSS class |
| `backRouter` | String \| Object | - | Back button router link |

### Slots

| Slot | Description |
|------|-------------|
| `default` | Breadcrumb items (`bk-breadcrumb-item`) |

---

## BreadcrumbItem (bk-breadcrumb-item)

Breadcrumb item.

### Props

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `to` | String \| Object | - | Vue router link |
| `replace` | Boolean | `false` | Use router.replace |
| `extCls` | String | `''` | External CSS class |

### Slots

| Slot | Description |
|------|-------------|
| `default` | Item content |

### Examples

```vue
<bk-breadcrumb separator="/">
  <bk-breadcrumb-item :to="{ path: '/' }">Home</bk-breadcrumb-item>
  <bk-breadcrumb-item :to="{ path: '/users' }">Users</bk-breadcrumb-item>
  <bk-breadcrumb-item>Detail</bk-breadcrumb-item>
</bk-breadcrumb>

<!-- With back router -->
<bk-breadcrumb :back-router="{ name: 'userList' }">
  <bk-breadcrumb-item>User Detail</bk-breadcrumb-item>
</bk-breadcrumb>

<!-- With icon separator -->
<bk-breadcrumb separator-class="bk-icon icon-angle-right">
  <bk-breadcrumb-item :to="'/'">Home</bk-breadcrumb-item>
  <bk-breadcrumb-item>Current</bk-breadcrumb-item>
</bk-breadcrumb>
```

---

## DropdownMenu (bk-dropdown-menu)

Dropdown menu component.

### Props

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `trigger` | String | `'click'` | Trigger: `'click'` \| `'hover'` |
| `align` | String | `'left'` | Alignment: `'left'` \| `'center'` \| `'right'` |
| `disabled` | Boolean | `false` | Disable dropdown |
| `fontSize` | String | `'normal'` | Font size: `'normal'` \| `'medium'` \| `'large'` |
| `positionFixed` | Boolean | `false` | Use position fixed |
| `extCls` | String | `''` | External CSS class |

### Events

| Event | Parameters | Description |
|-------|------------|-------------|
| `show` | - | Emitted when dropdown shows |
| `hide` | - | Emitted when dropdown hides |

### Slots

| Slot | Description |
|------|-------------|
| `dropdown-trigger` | Trigger element |
| `dropdown-content` | Dropdown content |

### Methods

| Method | Description |
|--------|-------------|
| `show()` | Show dropdown |
| `hide()` | Hide dropdown |

### Examples

```vue
<bk-dropdown-menu trigger="click">
  <template slot="dropdown-trigger">
    <bk-button>
      Dropdown <i class="bk-icon icon-angle-down"></i>
    </bk-button>
  </template>
  <template slot="dropdown-content">
    <ul class="bk-dropdown-list">
      <li><a href="javascript:;" @click="handleAction('edit')">Edit</a></li>
      <li><a href="javascript:;" @click="handleAction('delete')">Delete</a></li>
      <li class="bk-dropdown-item-disabled">Disabled</li>
    </ul>
  </template>
</bk-dropdown-menu>

<!-- Hover trigger -->
<bk-dropdown-menu trigger="hover" align="right">
  <template slot="dropdown-trigger">
    <span class="user-info">
      <i class="bk-icon icon-user"></i> Admin
    </span>
  </template>
  <template slot="dropdown-content">
    <ul class="bk-dropdown-list">
      <li><a @click="goProfile">Profile</a></li>
      <li><a @click="logout">Logout</a></li>
    </ul>
  </template>
</bk-dropdown-menu>
```

---

## Swiper (bk-swiper)

Carousel/swiper component.

### Props

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `list` | Array | `[]` | Slide data |
| `width` | Number | `400` | Swiper width |
| `height` | Number | `300` | Swiper height |
| `loopTime` | Number | `3000` | Auto play interval (ms), 0 = disabled |
| `isLoop` | Boolean | `true` | Enable loop |
| `extCls` | String | `''` | External CSS class |

### Events

| Event | Parameters | Description |
|-------|------------|-------------|
| `index-change` | `(index: Number)` | Emitted when slide changes |

### Slots

For each slide at index `i`:
- `{i}` - Custom slide content

### Examples

```vue
<bk-swiper :list="slides" :width="800" :height="400" :loop-time="5000" />

<script>
data() {
  return {
    slides: [
      { url: '/image1.jpg' },
      { url: '/image2.jpg' },
      { url: '/image3.jpg' }
    ]
  }
}
</script>

<!-- Custom slides -->
<bk-swiper :list="[1, 2, 3]" :width="600" :height="300">
  <template slot="0">
    <div class="custom-slide">Slide 1</div>
  </template>
  <template slot="1">
    <div class="custom-slide">Slide 2</div>
  </template>
</bk-swiper>
```
