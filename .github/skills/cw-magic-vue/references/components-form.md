# Form Components

## Input (bk-input)

Text input component with various modes and features.

### Props

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `type` | String | `'text'` | Input type: `'text'` \| `'password'` \| `'number'` \| `'email'` \| `'url'` \| `'date'` \| `'textarea'` |
| `value` / `v-model` | String \| Number | `''` | Input value |
| `placeholder` | String | `''` | Placeholder text |
| `disabled` | Boolean | `false` | Disable input |
| `readonly` | Boolean | `false` | Read-only mode |
| `clearable` | Boolean | `false` | Show clear button |
| `showPassword` | Boolean | `false` | Show password toggle (when `type: 'password'`) |
| `maxlength` | Number | - | Maximum input length |
| `minlength` | Number | - | Minimum input length |
| `size` | String | `''` | Input size: `''` \| `'large'` \| `'small'` |
| `prefixIcon` | String | `''` | Prefix icon class |
| `suffixIcon` | String | `''` | Suffix icon class |
| `rows` | Number | `2` | Rows for textarea |
| `showWordLimit` | Boolean | `false` | Show word count |
| `showClearOnlyHover` | Boolean | `false` | Only show clear on hover |
| `precision` | Number | - | Decimal precision (for number type) |
| `fontSize` | String | `'normal'` | Font size: `'normal'` \| `'medium'` \| `'large'` |
| `behavior` | String | `'normal'` | Behavior: `'normal'` \| `'simplicity'` |
| `nativeAttributes` | Object | `{}` | Native input attributes |
| `extCls` | String | `''` | External CSS class |

### Events

| Event | Parameters | Description |
|-------|------------|-------------|
| `input` | `(value: String)` | Emitted on input (for v-model) |
| `change` | `(value: String, event: Event)` | Emitted on value change (blur) |
| `focus` | `(event: FocusEvent)` | Emitted on focus |
| `blur` | `(event: FocusEvent)` | Emitted on blur |
| `keypress` | `(value: String, event: KeyboardEvent)` | Emitted on keypress |
| `keydown` | `(value: String, event: KeyboardEvent)` | Emitted on keydown |
| `keyup` | `(value: String, event: KeyboardEvent)` | Emitted on keyup |
| `enter` | `(value: String, event: KeyboardEvent)` | Emitted on Enter key |
| `paste` | `(value: String, event: ClipboardEvent)` | Emitted on paste |
| `clear` | - | Emitted when clear button clicked |
| `left-icon-click` | `(event: MouseEvent)` | Emitted when prefix icon clicked |
| `right-icon-click` | `(event: MouseEvent)` | Emitted when suffix icon clicked |

### Slots

| Slot | Description |
|------|-------------|
| `prepend` | Content prepended to input |
| `append` | Content appended to input |
| `prefix` | Prefix icon area |
| `suffix` | Suffix icon area |

### Methods

| Method | Parameters | Description |
|--------|------------|-------------|
| `focus()` | - | Focus the input |
| `blur()` | - | Blur the input |

### Examples

```vue
<!-- Basic input -->
<bk-input v-model="value" placeholder="Enter text" />

<!-- Password -->
<bk-input v-model="password" type="password" show-password />

<!-- Clearable -->
<bk-input v-model="value" clearable />

<!-- With icons -->
<bk-input v-model="search" prefix-icon="bk-icon icon-search" />
<bk-input v-model="email" suffix-icon="bk-icon icon-email" />

<!-- Textarea -->
<bk-input v-model="content" type="textarea" :rows="4" />

<!-- With word limit -->
<bk-input v-model="value" :maxlength="100" show-word-limit />

<!-- Prepend/Append -->
<bk-input v-model="url">
  <template slot="prepend">https://</template>
  <template slot="append">.com</template>
</bk-input>

<!-- Sizes -->
<bk-input v-model="value" size="large" />
<bk-input v-model="value" size="small" />
```

---

## InputNumber (bk-input-number)

Numeric input with step controls.

### Props

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `value` / `v-model` | Number | - | Input value |
| `min` | Number | `-Infinity` | Minimum value |
| `max` | Number | `Infinity` | Maximum value |
| `step` | Number | `1` | Step increment |
| `precision` | Number | - | Decimal precision |
| `disabled` | Boolean | `false` | Disable input |
| `controls` | Boolean | `true` | Show increment/decrement controls |
| `size` | String | `''` | Size: `''` \| `'large'` \| `'small'` |
| `showControls` | Boolean | `true` | Alias for `controls` |
| `initialControlsState` | String | `'normal'` | Initial state: `'normal'` \| `'plus'` \| `'minus'` |
| `extCls` | String | `''` | External CSS class |

### Events

| Event | Parameters | Description |
|-------|------------|-------------|
| `input` | `(value: Number)` | Emitted on input |
| `change` | `(value: Number, oldValue: Number)` | Emitted on value change |
| `focus` | `(event: FocusEvent)` | Emitted on focus |
| `blur` | `(event: FocusEvent)` | Emitted on blur |

### Examples

```vue
<!-- Basic -->
<bk-input-number v-model="num" />

<!-- With min/max -->
<bk-input-number v-model="num" :min="0" :max="100" />

<!-- With step -->
<bk-input-number v-model="num" :step="0.1" :precision="2" />

<!-- Without controls -->
<bk-input-number v-model="num" :controls="false" />
```

---

## Select (bk-select)

Dropdown select component with search and multiple selection support.

### Props

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `value` / `v-model` | Any | - | Selected value(s) |
| `multiple` | Boolean | `false` | Enable multiple selection |
| `disabled` | Boolean | `false` | Disable select |
| `clearable` | Boolean | `false` | Show clear button |
| `loading` | Boolean | `false` | Show loading state |
| `searchable` | Boolean | `false` | Enable search/filter |
| `remoteMethod` | Function | - | Remote search method |
| `placeholder` | String | `'请选择'` | Placeholder text |
| `size` | String | `'normal'` | Size: `'large'` \| `'normal'` \| `'small'` |
| `showSelectAll` | Boolean | `false` | Show "Select All" option (multiple mode) |
| `scrollHeight` | Number | `216` | Dropdown max height |
| `popoverMinWidth` | Number | - | Dropdown min width |
| `popoverWidth` | Number | - | Dropdown fixed width |
| `popoverOptions` | Object | `{}` | Popover configuration |
| `displayTag` | Boolean | `false` | Display selected items as tags (multiple mode) |
| `tagTheme` | String | `'info'` | Tag theme (multiple mode) |
| `autoHeight` | Boolean | `true` | Auto adjust height for tags |
| `collapseTag` | Boolean | `false` | Collapse excess tags |
| `showEmpty` | Boolean | `true` | Show empty state |
| `searchWithPinyin` | Boolean | `false` | Search with pinyin |
| `allowCreate` | Boolean | `false` | Allow creating new options |
| `allowEnter` | Boolean | `true` | Allow Enter key to select |
| `enableVirtualScroll` | Boolean | `false` | Enable virtual scroll |
| `list` | Array | `[]` | Options list (virtual scroll mode) |
| `idKey` | String | `'id'` | ID field key |
| `displayKey` | String | `'name'` | Display field key |
| `fontSize` | String | `'normal'` | Font size: `'normal'` \| `'medium'` \| `'large'` |
| `extCls` | String | `''` | External CSS class |
| `extPopoverCls` | String | `''` | Dropdown external class |

### Events

| Event | Parameters | Description |
|-------|------------|-------------|
| `input` | `(value)` | Emitted on selection (for v-model) |
| `change` | `(value, oldValue)` | Emitted on value change |
| `toggle` | `(isOpen: Boolean)` | Emitted when dropdown toggles |
| `selected` | `(value, option)` | Emitted when option selected |
| `clear` | `(oldValue)` | Emitted when cleared |
| `tab-remove` | `(value)` | Emitted when tag removed (multiple mode) |
| `scroll-end` | - | Emitted on scroll to bottom |

### Slots

| Slot | Description |
|------|-------------|
| `default` | Options (`bk-option` or `bk-option-group`) |
| `trigger` | Custom trigger content |
| `extension` | Extension content at dropdown bottom |

### Examples

```vue
<!-- Basic select -->
<bk-select v-model="selected" placeholder="Select option">
  <bk-option v-for="item in options" :key="item.id" :id="item.id" :name="item.name" />
</bk-select>

<!-- With search -->
<bk-select v-model="selected" searchable>
  <bk-option v-for="item in options" :key="item.id" :id="item.id" :name="item.name" />
</bk-select>

<!-- Multiple selection -->
<bk-select v-model="selected" multiple show-select-all display-tag collapse-tag>
  <bk-option v-for="item in options" :key="item.id" :id="item.id" :name="item.name" />
</bk-select>

<!-- Option groups -->
<bk-select v-model="selected">
  <bk-option-group label="Group 1">
    <bk-option id="1" name="Option 1" />
    <bk-option id="2" name="Option 2" />
  </bk-option-group>
  <bk-option-group label="Group 2">
    <bk-option id="3" name="Option 3" />
  </bk-option-group>
</bk-select>

<!-- Remote search -->
<bk-select v-model="selected" searchable :remote-method="fetchOptions" :loading="loading">
  <bk-option v-for="item in options" :key="item.id" :id="item.id" :name="item.name" />
</bk-select>

<!-- Allow create -->
<bk-select v-model="selected" searchable allow-create>
  <bk-option v-for="item in options" :key="item.id" :id="item.id" :name="item.name" />
</bk-select>
```

---

## Option (bk-option)

Option item for bk-select.

### Props

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `id` | Any | **required** | Option value |
| `name` | String | **required** | Option display text |
| `disabled` | Boolean | `false` | Disable option |

---

## OptionGroup (bk-option-group)

Option group for bk-select.

### Props

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `label` | String | `''` | Group label |
| `disabled` | Boolean | `false` | Disable all options in group |
| `showCollapse` | Boolean | `false` | Show collapse toggle |
| `collapse` | Boolean | `false` | Initial collapsed state |
| `showCount` | Boolean | `false` | Show option count |

---

## Checkbox (bk-checkbox)

Checkbox component for single or group selection.

### Props

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `value` / `v-model` | Boolean \| String \| Number | - | Checked state or value |
| `label` | String \| Number \| Boolean | - | Checkbox value (in group) |
| `trueValue` | String \| Number \| Boolean | `true` | Value when checked |
| `falseValue` | String \| Number \| Boolean | `false` | Value when unchecked |
| `disabled` | Boolean | `false` | Disable checkbox |
| `indeterminate` | Boolean | `false` | Indeterminate state |
| `checked` | Boolean | `false` | Initial checked state |
| `name` | String | - | Native name attribute |
| `extCls` | String | `''` | External CSS class |
| `beforeChange` | Function | - | Async validation before change (return true/false or Promise) |

### Events

| Event | Parameters | Description |
|-------|------------|-------------|
| `input` | `(value)` | Emitted on change (for v-model) |
| `change` | `(value, label)` | Emitted when checked state changes |

### Slots

| Slot | Description |
|------|-------------|
| `default` | Checkbox label content |

### Examples

```vue
<!-- Single checkbox -->
<bk-checkbox v-model="checked">Agree to terms</bk-checkbox>

<!-- With custom values -->
<bk-checkbox v-model="status" true-value="active" false-value="inactive">
  Active
</bk-checkbox>

<!-- Indeterminate -->
<bk-checkbox v-model="checkAll" :indeterminate="indeterminate" @change="handleCheckAll">
  Select All
</bk-checkbox>
```

---

## CheckboxGroup (bk-checkbox-group)

Group container for checkboxes.

### Props

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `value` / `v-model` | Array | `[]` | Selected values |
| `disabled` | Boolean | `false` | Disable all checkboxes |
| `name` | String | - | Native name for all checkboxes |

### Events

| Event | Parameters | Description |
|-------|------------|-------------|
| `input` | `(value: Array)` | Emitted on change (for v-model) |
| `change` | `(value: Array)` | Emitted when selection changes |

### Examples

```vue
<bk-checkbox-group v-model="selected">
  <bk-checkbox label="apple">Apple</bk-checkbox>
  <bk-checkbox label="banana">Banana</bk-checkbox>
  <bk-checkbox label="orange">Orange</bk-checkbox>
</bk-checkbox-group>
```

---

## Radio (bk-radio)

Radio button component.

### Props

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `value` / `v-model` | String \| Number \| Boolean | - | Radio value |
| `label` | String \| Number \| Boolean | - | Radio value (when in group) |
| `disabled` | Boolean | `false` | Disable radio |
| `checked` | Boolean | `false` | Initial checked state |
| `name` | String | - | Native name attribute |
| `extCls` | String | `''` | External CSS class |
| `beforeChange` | Function | - | Async validation before change |

### Events

| Event | Parameters | Description |
|-------|------------|-------------|
| `input` | `(value)` | Emitted on change (for v-model) |
| `change` | `(value, label)` | Emitted when selection changes |

### Slots

| Slot | Description |
|------|-------------|
| `default` | Radio label content |

---

## RadioGroup (bk-radio-group)

Group container for radio buttons.

### Props

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `value` / `v-model` | Any | - | Selected value |
| `disabled` | Boolean | `false` | Disable all radios |
| `name` | String | - | Native name for all radios |

### Events

| Event | Parameters | Description |
|-------|------------|-------------|
| `input` | `(value)` | Emitted on change (for v-model) |
| `change` | `(value)` | Emitted when selection changes |

### Examples

```vue
<bk-radio-group v-model="selected">
  <bk-radio label="option1">Option 1</bk-radio>
  <bk-radio label="option2">Option 2</bk-radio>
  <bk-radio label="option3">Option 3</bk-radio>
</bk-radio-group>

<!-- Radio buttons (button style) -->
<bk-radio-group v-model="selected">
  <bk-radio-button label="option1">Option 1</bk-radio-button>
  <bk-radio-button label="option2">Option 2</bk-radio-button>
</bk-radio-group>
```

---

## Switcher (bk-switcher)

Toggle switch component.

### Props

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `value` / `v-model` | Boolean \| String \| Number | `false` | Switch state |
| `disabled` | Boolean | `false` | Disable switch |
| `showText` | Boolean | `false` | Show ON/OFF text |
| `onText` | String | `'ON'` | Text when on |
| `offText` | String | `'OFF'` | Text when off |
| `trueValue` | Boolean \| String \| Number | `true` | Value when on |
| `falseValue` | Boolean \| String \| Number | `false` | Value when off |
| `size` | String | `''` | Size: `''` \| `'large'` \| `'small'` \| `'mini'` |
| `theme` | String | `'primary'` | Theme: `'primary'` \| `'success'` |
| `isOutline` | Boolean | `false` | Outline style |
| `isSquare` | Boolean | `false` | Square corners |
| `preCheck` | Function | - | Pre-check function before toggle |
| `extCls` | String | `''` | External CSS class |

### Events

| Event | Parameters | Description |
|-------|------------|-------------|
| `input` | `(value)` | Emitted on change (for v-model) |
| `change` | `(value)` | Emitted when state changes |

### Examples

```vue
<!-- Basic -->
<bk-switcher v-model="isActive" />

<!-- With text -->
<bk-switcher v-model="isActive" show-text />

<!-- Custom text -->
<bk-switcher v-model="isActive" show-text on-text="Yes" off-text="No" />

<!-- With pre-check -->
<bk-switcher v-model="isActive" :pre-check="handlePreCheck" />

<script>
methods: {
  async handlePreCheck() {
    return await this.$bkInfo({
      title: 'Confirm',
      subTitle: 'Are you sure?'
    })
  }
}
</script>
```

---

## DatePicker (bk-date-picker)

Date and time picker component.

### Props

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `value` / `v-model` | Date \| String \| Array | - | Selected date(s) |
| `type` | String | `'date'` | Picker type: `'date'` \| `'daterange'` \| `'datetime'` \| `'datetimerange'` \| `'month'` \| `'year'` |
| `format` | String | `'yyyy-MM-dd'` | Display format |
| `placeholder` | String | `'选择日期'` | Placeholder text |
| `disabled` | Boolean | `false` | Disable picker |
| `readonly` | Boolean | `false` | Read-only mode |
| `clearable` | Boolean | `true` | Show clear button |
| `editable` | Boolean | `true` | Allow manual input |
| `open` | Boolean | `null` | Control dropdown open state |
| `multiple` | Boolean | `false` | Allow multiple dates |
| `splitPanels` | Boolean | `true` | Split range panels |
| `showTime` | Boolean | `false` | Show time picker |
| `startDate` | Date | - | Default displayed start date |
| `placement` | String | `'bottom-start'` | Dropdown placement |
| `transfer` | Boolean | `false` | Transfer dropdown to body |
| `shortcuts` | Array | `[]` | Shortcut buttons |
| `shortcutClose` | Boolean | `false` | Close on shortcut click |
| `disabledDate` | Function | - | Function to disable dates |
| `timePickerOptions` | Object | `{}` | Time picker options |
| `options` | Object | `{}` | Additional options |
| `fontSize` | String | `'normal'` | Font size: `'normal'` \| `'medium'` \| `'large'` |
| `extCls` | String | `''` | External CSS class |
| `extPopoverCls` | String | `''` | Dropdown external class |
| `behavior` | String | `'normal'` | Behavior: `'normal'` \| `'simplicity'` |
| `upToNow` | Boolean | `false` | Allow selecting up to current time |
| `useShortcutText` | Boolean | `false` | Display shortcut text as value |

### Events

| Event | Parameters | Description |
|-------|------------|-------------|
| `input` | `(value)` | Emitted on change (for v-model) |
| `change` | `(value, type)` | Emitted when date changes |
| `open-change` | `(isOpen: Boolean)` | Emitted when dropdown opens/closes |
| `pick-success` | - | Emitted after successful pick |
| `clear` | - | Emitted when cleared |
| `shortcut-change` | `(shortcut, picker)` | Emitted when shortcut clicked |

### Examples

```vue
<!-- Basic date picker -->
<bk-date-picker v-model="date" placeholder="Select date" />

<!-- Date range -->
<bk-date-picker v-model="dateRange" type="daterange" />

<!-- DateTime -->
<bk-date-picker v-model="datetime" type="datetime" />

<!-- With shortcuts -->
<bk-date-picker v-model="date" :shortcuts="shortcuts" />

<script>
data() {
  return {
    shortcuts: [
      {
        text: 'Today',
        value: () => new Date()
      },
      {
        text: 'Yesterday',
        value: () => {
          const date = new Date()
          date.setDate(date.getDate() - 1)
          return date
        }
      },
      {
        text: 'Last 7 days',
        value: () => {
          const end = new Date()
          const start = new Date()
          start.setDate(start.getDate() - 7)
          return [start, end]
        }
      }
    ]
  }
}
</script>

<!-- Disabled dates -->
<bk-date-picker v-model="date" :disabled-date="disabledDate" />

<script>
methods: {
  disabledDate(date) {
    return date < new Date() // Disable past dates
  }
}
</script>
```

---

## TimePicker (bk-time-picker)

Time picker component.

### Props

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `value` / `v-model` | Date \| String \| Array | - | Selected time(s) |
| `type` | String | `'time'` | Picker type: `'time'` \| `'timerange'` |
| `format` | String | `'HH:mm:ss'` | Display format |
| `placeholder` | String | `'选择时间'` | Placeholder text |
| `disabled` | Boolean | `false` | Disable picker |
| `clearable` | Boolean | `true` | Show clear button |
| `editable` | Boolean | `true` | Allow manual input |
| `open` | Boolean | `null` | Control dropdown open state |
| `placement` | String | `'bottom-start'` | Dropdown placement |
| `transfer` | Boolean | `false` | Transfer dropdown to body |
| `steps` | Array | `[]` | Hour/minute/second steps |
| `allowCrossDay` | Boolean | `false` | Allow time range across days |
| `extCls` | String | `''` | External CSS class |

### Events

| Event | Parameters | Description |
|-------|------------|-------------|
| `input` | `(value)` | Emitted on change (for v-model) |
| `change` | `(value)` | Emitted when time changes |
| `open-change` | `(isOpen: Boolean)` | Emitted when dropdown opens/closes |
| `clear` | - | Emitted when cleared |

### Examples

```vue
<!-- Basic time picker -->
<bk-time-picker v-model="time" />

<!-- Time range -->
<bk-time-picker v-model="timeRange" type="timerange" />

<!-- Custom format -->
<bk-time-picker v-model="time" format="HH:mm" />

<!-- With steps -->
<bk-time-picker v-model="time" :steps="[1, 15, 30]" />
```

---

## Form (bk-form)

Form container with validation support.

### Props

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `model` | Object | **required** | Form data object |
| `rules` | Object | `{}` | Validation rules |
| `labelWidth` | Number \| String | - | Label width |
| `labelPosition` | String | `'right'` | Label position: `'left'` \| `'right'` \| `'top'` |
| `formType` | String | `'horizontal'` | Layout type: `'horizontal'` \| `'vertical'` \| `'inline'` |
| `extCls` | String | `''` | External CSS class |

### Events

| Event | Parameters | Description |
|-------|------------|-------------|
| `validate` | `(isValid: Boolean, invalidFields: Object)` | Emitted after validation |

### Methods

| Method | Parameters | Returns | Description |
|--------|------------|---------|-------------|
| `validate(fields?)` | `fields?: String[]` | `Promise<void>` | Validate form (resolves on success, rejects with validator on fail) |
| `clearError(fields?)` | `fields?: String[]` | - | Clear validation errors |

### Slots

| Slot | Description |
|------|-------------|
| `default` | Form items (`bk-form-item`) |

### Validation Rules

```javascript
rules: {
  fieldName: [
    { required: true, message: 'Required field', trigger: 'blur' },
    { min: 3, max: 10, message: '3-10 characters', trigger: 'blur' },
    { regex: /^[a-z]+$/, message: 'Lowercase letters only', trigger: 'blur' },
    { validator: (val) => val > 0, message: 'Must be positive', trigger: 'change' },
    { validator: async (val) => await checkUnique(val), message: 'Already exists', trigger: 'blur' }
  ]
}
```

---

## FormItem (bk-form-item)

Form item wrapper with label and validation.

### Props

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `property` | String | - | Field name in form model (for validation) |
| `label` | String | - | Label text |
| `labelWidth` | Number \| String | - | Label width (overrides form) |
| `required` | Boolean | `false` | Show required asterisk |
| `rules` | Array | - | Validation rules (overrides form rules) |
| `errorDisplayType` | String | `'normal'` | Error display: `'normal'` \| `'tooltips'` |
| `extCls` | String | `''` | External CSS class |
| `desc` | String | - | Description text |
| `descType` | String | `'border'` | Description type: `'border'` \| `'icon'` |
| `descIcon` | String | `'bk-icon icon-info'` | Description icon |
| `autoCheck` | Boolean | `false` | Auto validate on mount |
| `iconOffset` | Number | `8` | Required icon offset |

### Slots

| Slot | Description |
|------|-------------|
| `default` | Form control |
| `tip` | Custom error tip |
| `desc` | Custom description |

### Examples

```vue
<bk-form :model="formData" :rules="rules" ref="form" label-width="100">
  <bk-form-item label="Username" property="username" required>
    <bk-input v-model="formData.username" placeholder="Enter username" />
  </bk-form-item>
  
  <bk-form-item label="Email" property="email" required>
    <bk-input v-model="formData.email" placeholder="Enter email" />
  </bk-form-item>
  
  <bk-form-item label="Gender" property="gender">
    <bk-radio-group v-model="formData.gender">
      <bk-radio label="male">Male</bk-radio>
      <bk-radio label="female">Female</bk-radio>
    </bk-radio-group>
  </bk-form-item>
  
  <bk-form-item>
    <bk-button theme="primary" @click="handleSubmit">Submit</bk-button>
    <bk-button @click="handleReset">Reset</bk-button>
  </bk-form-item>
</bk-form>

<script>
export default {
  data() {
    return {
      formData: {
        username: '',
        email: '',
        gender: ''
      },
      rules: {
        username: [
          { required: true, message: 'Username is required', trigger: 'blur' },
          { min: 3, max: 20, message: '3-20 characters', trigger: 'blur' }
        ],
        email: [
          { required: true, message: 'Email is required', trigger: 'blur' },
          { regex: /^[\w-]+@[\w-]+\.\w+$/, message: 'Invalid email', trigger: 'blur' }
        ]
      }
    }
  },
  methods: {
    handleSubmit() {
      this.$refs.form.validate().then(() => {
        // Submit form
        console.log('Form valid:', this.formData)
      }).catch(validator => {
        // Show first error
        console.log('Validation failed:', validator)
      })
    },
    handleReset() {
      this.formData = { username: '', email: '', gender: '' }
      this.$refs.form.clearError()
    }
  }
}
</script>
```

---

## Slider (bk-slider)

Slider component for selecting values within a range.

### Props

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `value` / `v-model` | Number \| Array | `0` | Current value(s) |
| `min` | Number | `0` | Minimum value |
| `max` | Number | `100` | Maximum value |
| `step` | Number | `1` | Step increment |
| `range` | Boolean | `false` | Enable range selection |
| `vertical` | Boolean | `false` | Vertical orientation |
| `height` | String | `'200px'` | Height (vertical mode) |
| `disabled` | Boolean | `false` | Disable slider |
| `showTip` | Boolean | `true` | Show value tooltip |
| `showInterval` | Boolean | `false` | Show interval marks |
| `showIntervalLabel` | Boolean | `false` | Show interval labels |
| `showButtonLabel` | Boolean | `false` | Show button value label |
| `showBetweenLabel` | Boolean | `false` | Show between labels |
| `showInput` | Boolean | `false` | Show input box |
| `customContent` | Object | - | Custom content (marks) |
| `extCls` | String | `''` | External CSS class |

### Events

| Event | Parameters | Description |
|-------|------------|-------------|
| `input` | `(value)` | Emitted on change (for v-model) |
| `change` | `(value)` | Emitted after drag ends |

### Examples

```vue
<!-- Basic slider -->
<bk-slider v-model="value" />

<!-- With range -->
<bk-slider v-model="range" range :min="0" :max="100" />

<!-- With input -->
<bk-slider v-model="value" show-input />

<!-- With marks -->
<bk-slider v-model="value" :custom-content="marks" />

<script>
data() {
  return {
    marks: {
      0: '0°C',
      25: '25°C',
      50: '50°C',
      75: '75°C',
      100: '100°C'
    }
  }
}
</script>
```

---

## Rate (bk-rate)

Star rating component.

### Props

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `value` / `v-model` | Number | `0` | Current rating |
| `max` | Number | `5` | Maximum stars |
| `disabled` | Boolean | `false` | Disable rating |
| `editable` | Boolean | `true` | Allow editing |
| `width` | Number | `16` | Star width (px) |
| `height` | Number | `16` | Star height (px) |
| `tooltips` | Array | `[]` | Tooltip for each level |
| `showScore` | Boolean | `false` | Show score text |
| `extCls` | String | `''` | External CSS class |

### Events

| Event | Parameters | Description |
|-------|------------|-------------|
| `input` | `(value: Number)` | Emitted on change (for v-model) |
| `change` | `(value: Number)` | Emitted when rating changes |

### Examples

```vue
<!-- Basic -->
<bk-rate v-model="rating" />

<!-- With tooltips -->
<bk-rate v-model="rating" :tooltips="['Very Bad', 'Bad', 'OK', 'Good', 'Excellent']" />

<!-- With score -->
<bk-rate v-model="rating" show-score />

<!-- Read only -->
<bk-rate :value="4.5" :editable="false" />
```

---

## ColorPicker (bk-color-picker)

Color picker component.

### Props

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `value` / `v-model` | String | `''` | Selected color (hex/rgb/rgba) |
| `disabled` | Boolean | `false` | Disable picker |
| `transfer` | Boolean | `false` | Transfer dropdown to body |
| `size` | String | `'default'` | Size: `'default'` \| `'large'` \| `'small'` |
| `showValue` | Boolean | `true` | Show color value |
| `recommend` | Boolean | `true` | Show recommended colors |
| `recommendColors` | Array | - | Custom recommended colors |
| `extCls` | String | `''` | External CSS class |

### Events

| Event | Parameters | Description |
|-------|------------|-------------|
| `input` | `(color: String)` | Emitted on change (for v-model) |
| `change` | `(color: String)` | Emitted when color changes |

### Examples

```vue
<bk-color-picker v-model="color" />

<!-- With custom recommended colors -->
<bk-color-picker v-model="color" :recommend-colors="['#ff0000', '#00ff00', '#0000ff']" />
```

---

## Upload (bk-upload)

File upload component.

### Props

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `url` | String | `''` | Upload URL |
| `name` | String | `'upload_file'` | File field name |
| `accept` | String | - | Accepted file types |
| `multiple` | Boolean | `false` | Allow multiple files |
| `limit` | Number | - | Maximum file count |
| `size` | Object | - | Size limit `{ maxFileSize, maxImgSize }` |
| `handleResCode` | Function | - | Response code handler |
| `header` | Object | `{}` | Request headers |
| `formDataAttributes` | Array | `[]` | Extra form data |
| `withCredentials` | Boolean | `false` | Send credentials |
| `files` | Array | `[]` | File list (v-model) |
| `theme` | String | `'draggable'` | Theme: `'draggable'` \| `'picture'` \| `'button'` |
| `tip` | String | - | Upload tip text |
| `delayTime` | Number | `0` | Upload delay |
| `validateName` | RegExp | - | File name validation regex |
| `customRequest` | Function | - | Custom upload function |
| `disabled` | Boolean | `false` | Disable upload |
| `autoUpload` | Boolean | `true` | Auto upload on select |
| `extCls` | String | `''` | External CSS class |

### Events

| Event | Parameters | Description |
|-------|------------|-------------|
| `on-done` | `(fileList, responseData)` | Emitted when upload completes |
| `on-progress` | `(event, file, fileList)` | Emitted on upload progress |
| `on-success` | `(file, fileList)` | Emitted on single file success |
| `on-error` | `(file, fileList, error)` | Emitted on error |
| `on-exceed` | `(file, fileList)` | Emitted when limit exceeded |
| `on-delete` | `(file, fileList)` | Emitted when file deleted |

### Examples

```vue
<!-- Draggable upload -->
<bk-upload
  url="/api/upload"
  :tip="'Support JPG, PNG files'"
  accept=".jpg,.jpeg,.png"
/>

<!-- Button upload -->
<bk-upload
  theme="button"
  url="/api/upload"
/>

<!-- Picture upload -->
<bk-upload
  theme="picture"
  url="/api/upload"
  multiple
  :limit="5"
/>

<!-- Custom upload -->
<bk-upload :custom-request="handleUpload">
  <bk-button>Upload</bk-button>
</bk-upload>

<script>
methods: {
  async handleUpload({ file, onProgress, onSuccess, onError }) {
    const formData = new FormData()
    formData.append('file', file)
    try {
      const response = await axios.post('/api/upload', formData, {
        onUploadProgress: ({ loaded, total }) => {
          onProgress({ percent: Math.round(loaded / total * 100) })
        }
      })
      onSuccess(response.data)
    } catch (error) {
      onError(error)
    }
  }
}
</script>
```

---

## TagInput (bk-tag-input)

Tag input component for entering multiple tags.

### Props

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `value` / `v-model` | Array | `[]` | Tag values |
| `list` | Array | `[]` | Suggestion list |
| `placeholder` | String | `''` | Placeholder text |
| `disabled` | Boolean | `false` | Disable input |
| `hasDeleteIcon` | Boolean | `true` | Show delete icon on tags |
| `clearable` | Boolean | `true` | Show clear all button |
| `allowCreate` | Boolean | `false` | Allow creating new tags |
| `allowAutoMatch` | Boolean | `false` | Auto match from list |
| `maxData` | Number | `-1` | Maximum tags (-1 = unlimited) |
| `maxResult` | Number | `10` | Maximum suggestions shown |
| `useGroup` | Boolean | `false` | Group suggestions |
| `contentMaxHeight` | Number | `300` | Max height for suggestions |
| `separator` | String | - | Tag separator (for paste) |
| `displayKey` | String | `'name'` | Display field key |
| `saveKey` | String | `'id'` | Value field key |
| `searchKey` | String \| Array | `'name'` | Search field key(s) |
| `trigger` | String | `'focus'` | Show suggestions: `'focus'` \| `'search'` |
| `filterCallback` | Function | - | Custom filter function |
| `createTagValidator` | Function | - | Validate new tag |
| `pasteFn` | Function | - | Custom paste handler |
| `tooltipKey` | String | - | Tooltip field key |
| `showClearOnlyHover` | Boolean | `false` | Only show clear button on hover |
| `collapseTags` | Boolean | `false` | Collapse tags when unfocused (fixed 32px height, shows +N for overflow, hover +N shows tooltip with hidden tag names, expands on focus) |
| `extCls` | String | `''` | External CSS class |

### Events

| Event | Parameters | Description |
|-------|------------|-------------|
| `input` | `(value: Array)` | Emitted on change (for v-model) |
| `change` | `(value: Array)` | Emitted when tags change |
| `select` | `(item, index)` | Emitted when suggestion selected |
| `remove` | `(item, index)` | Emitted when tag removed |
| `removeAll` | - | Emitted when all tags removed |
| `blur` | `(value, event)` | Emitted on blur |
| `focus` | `(value, event)` | Emitted on focus |

### Examples

```vue
<!-- Basic tag input -->
<bk-tag-input v-model="tags" :list="suggestions" placeholder="Add tags" />

<!-- Allow create -->
<bk-tag-input v-model="tags" allow-create />

<!-- With max limit -->
<bk-tag-input v-model="tags" :list="suggestions" :max-data="5" />

<!-- Collapse tags (fixed height, expands on focus) -->
<bk-tag-input 
  v-model="tags" 
  :list="suggestions" 
  :collapse-tags="true"
  trigger="focus"
  style="width: 200px;"
/>
```

---

## Cascade (bk-cascade)

Cascader component for hierarchical selection.

### Props

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `value` / `v-model` | Array | `[]` | Selected path values |
| `list` | Array | `[]` | Options data (tree structure) |
| `placeholder` | String | `'请选择'` | Placeholder text |
| `disabled` | Boolean | `false` | Disable cascader |
| `clearable` | Boolean | `false` | Show clear button |
| `multiple` | Boolean | `false` | Multiple selection |
| `checkAnyLevel` | Boolean | `false` | Allow selecting any level |
| `filterable` | Boolean | `false` | Enable filtering |
| `filterMethod` | Function | - | Custom filter function |
| `trigger` | String | `'click'` | Expand trigger: `'click'` \| `'hover'` |
| `isRemote` | Boolean | `false` | Remote loading |
| `remoteMethod` | Function | - | Remote load function |
| `separator` | String | `'/'` | Display separator |
| `idKey` | String | `'id'` | ID field key |
| `nameKey` | String | `'name'` | Name field key |
| `childrenKey` | String | `'children'` | Children field key |
| `scrollHeight` | Number | `216` | Panel max height |
| `scrollWidth` | Number | `160` | Panel width |
| `extCls` | String | `''` | External CSS class |
| `extPopoverCls` | String | `''` | Dropdown external class |

### Events

| Event | Parameters | Description |
|-------|------------|-------------|
| `input` | `(value: Array)` | Emitted on change (for v-model) |
| `change` | `(value, nodes, nodeArrays)` | Emitted when selection changes |
| `toggle` | `(isOpen: Boolean)` | Emitted when dropdown toggles |
| `clear` | - | Emitted when cleared |

### Examples

```vue
<bk-cascade v-model="selected" :list="options" />

<script>
data() {
  return {
    options: [
      {
        id: 'guangdong',
        name: 'Guangdong',
        children: [
          {
            id: 'shenzhen',
            name: 'Shenzhen',
            children: [
              { id: 'nanshan', name: 'Nanshan' },
              { id: 'futian', name: 'Futian' }
            ]
          }
        ]
      }
    ]
  }
}
</script>
```

---

## SearchSelect (bk-search-select)

Advanced search select with complex condition support.

### Props

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `data` | Array | `[]` | Search condition definitions |
| `values` | Array | `[]` | Selected conditions (v-model) |
| `placeholder` | String | - | Placeholder text |
| `maxHeight` | Number | `120` | Max input height |
| `minHeight` | Number | `32` | Min input height |
| `displayKey` | String | `'name'` | Display field |
| `primaryKey` | String | `'id'` | Primary key field |
| `showCondition` | Boolean | `true` | Show condition labels |
| `showPopoverTagChange` | Boolean | `true` | Show popover on tag change |
| `wrapZindex` | Number | `9` | Dropdown z-index |
| `defaultFocus` | Boolean | `false` | Auto focus on mount |
| `strink` | Boolean | `false` | Shrink mode |
| `readonly` | Boolean | `false` | Read-only mode |
| `filter` | Boolean | `false` | Enable filtering |
| `remoteMethod` | Function | - | Remote search method |
| `remoteEmptyText` | String | - | Empty text for remote |
| `getMenuList` | Function | - | Custom menu list getter |
| `validateValues` | Function | - | Validate selected values |
| `extCls` | String | `''` | External CSS class |

### Events

| Event | Parameters | Description |
|-------|------------|-------------|
| `change` | `(values)` | Emitted when conditions change |
| `key-enter` | `(values)` | Emitted on Enter key |
| `input-change` | `(keyword)` | Emitted on input change |
| `input-click-outside` | `(values)` | Emitted on click outside |
| `menu-child-condition-select` | `(item, index)` | Emitted when child selected |
| `menu-select` | `(item, index)` | Emitted when menu item selected |

### Data Structure

```javascript
data: [
  {
    id: 'status',
    name: 'Status',
    multiable: true,  // Allow multiple values
    children: [
      { id: 'active', name: 'Active' },
      { id: 'inactive', name: 'Inactive' }
    ]
  },
  {
    id: 'keyword',
    name: 'Keyword',
    // No children = free text input
  },
  {
    id: 'date',
    name: 'Date',
    remoteMethod: async (keyword) => {
      // Return filtered options
      return [{ id: '2024-01-01', name: '2024-01-01' }]
    }
  }
]
```

### Examples

```vue
<bk-search-select
  :data="searchData"
  :values="searchValues"
  @change="handleSearch"
/>
```
