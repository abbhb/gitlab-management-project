---
name: cw-magic-vue
description: |
  基于蓝鲸 Magicbox 的 Vue 2 组件库 (@canway/cw-magic-vue v3.8.156)。
  当项目中使用 @canway/cw-magic-vue 组件时使用此技能。
  提供 90+ 个 UI 组件，包括：Button、Select、Table、Form、Dialog、
  Message、Pagination、Tree、DatePicker、Upload、Navigation、Tab 等。
  所有组件使用 'bk-' 前缀（如 bk-button、bk-select、bk-table）。
---

# @canway/cw-magic-vue 组件库

基于蓝鲸 Magicbox 的 Vue 2.x 组件库。所有组件使用 `bk-` 前缀。

## 快速开始

### 安装
```bash
npm install @canway/cw-magic-vue
```

### 全量引入
```javascript
import Vue from 'vue'
import bkMagicVue from '@canway/cw-magic-vue'
import '@canway/cw-magic-vue/dist/bk-magic-vue.min.css'

Vue.use(bkMagicVue)
```

### 按需引入
```javascript
import { bkButton, bkInput, bkTable } from '@canway/cw-magic-vue'
import '@canway/cw-magic-vue/dist/bk-magic-vue.min.css'

Vue.component('bk-button', bkButton)
Vue.component('bk-input', bkInput)
Vue.component('bk-table', bkTable)
```

## 组件分类

| 分类 | 组件 |
|------|------|
| **基础** | Button, Icon, Link, Tag, Badge, Divider |
| **表单** | Input, InputNumber, Select, Checkbox, Radio, Switcher, DatePicker, TimePicker, ColorPicker, Form, FormItem, Slider, Rate, Upload, TagInput, Cascade, SearchSelect |
| **数据展示** | Table, TableColumn, Pagination, Tree, BigTree, Collapse, Card, Description, Timeline, Diff, Progress, RoundProgress, VirtualScroll |
| **反馈** | Message, Notify, Dialog, Sideslider, Loading, Spin, InfoBox, Popconfirm, Popover, Exception, Alert |
| **导航** | Navigation, NavigationMenu, Tab, Steps, Breadcrumb, DropdownMenu |
| **布局** | Container, Row, Col, ResizeLayout |

## 指令

| 指令 | 用途 |
|------|------|
| `v-bk-tooltips` | 悬停提示 |
| `v-bkloading` | 加载遮罩 |
| `v-bk-clickoutside` | 检测元素外部点击 |
| `v-bk-overflow-tips` | 文本溢出时显示提示 |
| `v-bk-copy` | 复制文本到剪贴板 |
| `v-bk-resize` | 检测元素尺寸变化 |

## 常用示例

### 表单验证
```vue
<template>
  <bk-form :model="formData" :rules="rules" ref="form">
    <bk-form-item label="用户名" property="username" required>
      <bk-input v-model="formData.username" placeholder="请输入用户名" />
    </bk-form-item>
    <bk-form-item label="邮箱" property="email" required>
      <bk-input v-model="formData.email" placeholder="请输入邮箱" />
    </bk-form-item>
    <bk-form-item>
      <bk-button theme="primary" @click="handleSubmit">提交</bk-button>
    </bk-form-item>
  </bk-form>
</template>

<script>
export default {
  data() {
    return {
      formData: { username: '', email: '' },
      rules: {
        username: [{ required: true, message: '用户名不能为空', trigger: 'blur' }],
        email: [
          { required: true, message: '邮箱不能为空', trigger: 'blur' },
          { regex: /^[\w-]+@[\w-]+\.\w+$/, message: '邮箱格式不正确', trigger: 'blur' }
        ]
      }
    }
  },
  methods: {
    handleSubmit() {
      this.$refs.form.validate().then(() => {
        // 表单验证通过
      }).catch(validator => {
        // 验证失败
      })
    }
  }
}
</script>
```

### 表格分页
```vue
<template>
  <div>
    <bk-table :data="tableData" :pagination="pagination" @page-change="handlePageChange">
      <bk-table-column label="姓名" prop="name" />
      <bk-table-column label="年龄" prop="age" sortable />
      <bk-table-column label="操作">
        <template slot-scope="{ row }">
          <bk-button text theme="primary" @click="handleEdit(row)">编辑</bk-button>
          <bk-button text theme="danger" @click="handleDelete(row)">删除</bk-button>
        </template>
      </bk-table-column>
    </bk-table>
  </div>
</template>

<script>
export default {
  data() {
    return {
      tableData: [],
      pagination: {
        current: 1,
        count: 100,
        limit: 10
      }
    }
  },
  methods: {
    handlePageChange(page) {
      this.pagination.current = page
      this.fetchData()
    }
  }
}
</script>
```

### 对话框
```vue
<template>
  <div>
    <bk-button @click="showDialog = true">打开对话框</bk-button>
    <bk-dialog
      v-model="showDialog"
      title="确认操作"
      :confirm-fn="handleConfirm"
    >
      <p>确定要执行此操作吗？</p>
    </bk-dialog>
  </div>
</template>

<script>
export default {
  data() {
    return { showDialog: false }
  },
  methods: {
    async handleConfirm() {
      // 返回 true 关闭对话框，返回 false 保持打开
      await this.doSomething()
      return true
    }
  }
}
</script>
```

### 编程式 API

#### Message 消息提示
```javascript
// 成功消息
this.$bkMessage({ theme: 'success', message: '操作成功！' })

// 错误消息
this.$bkMessage({ theme: 'error', message: '操作失败！', delay: 5000 })

// 带关闭回调
this.$bkMessage({
  theme: 'warning',
  message: '警告消息',
  onClose: () => console.log('已关闭')
})
```

#### Notify 通知
```javascript
this.$bkNotify({
  title: '通知',
  message: '这是一条通知消息',
  theme: 'success',
  position: 'top-right',
  delay: 3000
})
```

#### InfoBox 确认框
```javascript
this.$bkInfo({
  title: '确认删除',
  subTitle: '确定要删除此项吗？',
  confirmFn: async () => {
    await this.deleteItem()
  },
  cancelFn: () => {
    console.log('已取消')
  }
})
```

#### Loading 加载
```javascript
// 显示加载
const loading = this.$bkLoading({ title: '加载中...' })

// 隐藏加载
loading.hide()

// 或使用指令
// <div v-bkloading="{ isLoading: true, title: '加载中...' }">
```

## 主题定制

组件库使用 CSS 变量进行主题定制。有两种方式：

### 使用 useTheme() API
```javascript
import theme from '@canway/cw-magic-vue/lib/ui/theme'

// 覆盖特定变量
theme.useTheme({
  '--brand': '#1272FF',           // 品牌基础色（生成 --primary-1 到 --primary-7）
  '--primary-6': '#1272FF',       // 主色（用于按钮、链接等）
  '--border-radius-2': '4px',     // 默认圆角
  '--size-default': '32px'        // 默认组件尺寸
})
```

### 直接使用 CSS 变量
```css
:root {
  /* 功能色（生成 1-7 色阶） */
  --brand: #1272FF;    /* 主色/品牌色 */
  --green: #27C274;    /* 成功 */
  --orange: #FF9214;   /* 警告 */
  --red: #F43B2C;      /* 错误/危险 */
  
  /* 或覆盖特定色阶颜色 */
  --primary-6: #1272FF;
  --success-6: #27C274;
  --warning-6: #FF9214;
  --danger-6: #F43B2C;
}
```

### 主要变量分类
- **颜色**: `--primary-1` 到 `--primary-7`, `--grey-1` 到 `--grey-10`
- **文字**: `--color-text-1`（主要）到 `--color-text-4`（禁用）
- **边框**: `--color-border-1` 到 `--color-border-4`
- **背景**: `--color-bg-1` 到 `--color-bg-7`
- **字号**: `--font-size-1`（12px）到 `--font-size-6`（24px）
- **圆角**: `--border-radius-0`（0）到 `--border-radius-3`（8px）
- **尺寸**: `--size-mini`（24px）, `--size-small`（26px）, `--size-default`（32px）, `--size-large`（34px）

### 组件变量命名规则
模式: `--{component}-{property}-{state1}-{state2}`
```css
--btn-bg-primary         /* 按钮主色背景 */
--btn-bg-primary-hover   /* 按钮主色悬停背景 */
--btn-text-warning-active /* 按钮警告文字激活态 */
```

## 参考文档

组件详细 API 请参阅：
- `references/components-basic.md` - 基础组件
- `references/components-form.md` - 表单组件
- `references/components-data.md` - 数据展示组件
- `references/components-feedback.md` - 反馈组件
- `references/components-navigation.md` - 导航组件
- `references/components-layout.md` - 布局组件
- `references/directives.md` - 指令
- `references/patterns.md` - 组件组合模式
