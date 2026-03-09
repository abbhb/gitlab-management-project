# 组件组合模式

常用的组件组合使用模式。

## 表单模式

### 完整表单验证

```vue
<template>
  <bk-form :model="formData" :rules="rules" ref="form" label-width="120">
    <bk-form-item label="用户名" property="username" required>
      <bk-input v-model="formData.username" placeholder="请输入用户名" />
    </bk-form-item>
    
    <bk-form-item label="邮箱" property="email" required>
      <bk-input v-model="formData.email" placeholder="请输入邮箱" />
    </bk-form-item>
    
    <bk-form-item label="部门" property="department" required>
      <bk-select v-model="formData.department" placeholder="请选择部门" searchable>
        <bk-option v-for="dept in departments" :key="dept.id" :id="dept.id" :name="dept.name" />
      </bk-select>
    </bk-form-item>
    
    <bk-form-item label="角色" property="role" required>
      <bk-radio-group v-model="formData.role">
        <bk-radio label="admin">管理员</bk-radio>
        <bk-radio label="user">普通用户</bk-radio>
        <bk-radio label="guest">访客</bk-radio>
      </bk-radio-group>
    </bk-form-item>
    
    <bk-form-item label="权限" property="permissions">
      <bk-checkbox-group v-model="formData.permissions">
        <bk-checkbox label="read">读取</bk-checkbox>
        <bk-checkbox label="write">写入</bk-checkbox>
        <bk-checkbox label="delete">删除</bk-checkbox>
      </bk-checkbox-group>
    </bk-form-item>
    
    <bk-form-item label="启用" property="active">
      <bk-switcher v-model="formData.active" />
    </bk-form-item>
    
    <bk-form-item label="开始日期" property="startDate">
      <bk-date-picker v-model="formData.startDate" placeholder="选择日期" />
    </bk-form-item>
    
    <bk-form-item>
      <bk-button theme="primary" :loading="submitting" @click="handleSubmit">
        提交
      </bk-button>
      <bk-button @click="handleReset">重置</bk-button>
    </bk-form-item>
  </bk-form>
</template>

<script>
export default {
  data() {
    return {
      formData: {
        username: '',
        email: '',
        department: '',
        role: '',
        permissions: [],
        active: true,
        startDate: ''
      },
      rules: {
        username: [
          { required: true, message: '用户名不能为空', trigger: 'blur' },
          { min: 3, max: 20, message: '长度在 3-20 个字符', trigger: 'blur' }
        ],
        email: [
          { required: true, message: '邮箱不能为空', trigger: 'blur' },
          { regex: /^[\w-]+@[\w-]+\.\w+$/, message: '邮箱格式不正确', trigger: 'blur' }
        ],
        department: [
          { required: true, message: '请选择部门', trigger: 'change' }
        ],
        role: [
          { required: true, message: '请选择角色', trigger: 'change' }
        ]
      },
      submitting: false,
      departments: []
    }
  },
  methods: {
    async handleSubmit() {
      try {
        await this.$refs.form.validate()
        this.submitting = true
        await this.saveForm()
        this.$bkMessage({ theme: 'success', message: '保存成功！' })
      } catch (validator) {
        // 验证失败
      } finally {
        this.submitting = false
      }
    },
    handleReset() {
      this.formData = {
        username: '', email: '', department: '', role: '',
        permissions: [], active: true, startDate: ''
      }
      this.$refs.form.clearError()
    }
  }
}
</script>
```

### 行内搜索表单

```vue
<bk-form :model="searchForm" form-type="inline">
  <bk-form-item label="关键字">
    <bk-input v-model="searchForm.keyword" placeholder="搜索..." clearable />
  </bk-form-item>
  <bk-form-item label="状态">
    <bk-select v-model="searchForm.status" placeholder="全部" clearable>
      <bk-option id="active" name="启用" />
      <bk-option id="inactive" name="禁用" />
    </bk-select>
  </bk-form-item>
  <bk-form-item label="日期">
    <bk-date-picker v-model="searchForm.dateRange" type="daterange" />
  </bk-form-item>
  <bk-form-item>
    <bk-button theme="primary" @click="handleSearch">搜索</bk-button>
    <bk-button @click="handleReset">重置</bk-button>
  </bk-form-item>
</bk-form>
```

---

## 表格模式

### 表格增删改查

```vue
<template>
  <div class="table-container">
    <!-- 工具栏 -->
    <div class="table-toolbar">
      <bk-button theme="primary" icon="icon-plus" @click="handleCreate">
        新增
      </bk-button>
      <bk-button :disabled="!selectedRows.length" @click="handleBatchDelete">
        批量删除
      </bk-button>
    </div>
    
    <!-- 表格 -->
    <bk-table
      :data="tableData"
      v-bkloading="{ isLoading: loading }"
      @selection-change="handleSelectionChange"
    >
      <bk-table-column type="selection" width="60" />
      <bk-table-column prop="name" label="名称" sortable show-overflow-tooltip />
      <bk-table-column prop="status" label="状态" width="120">
        <template slot-scope="{ row }">
          <bk-tag :theme="row.status === 'active' ? 'success' : 'danger'">
            {{ row.status }}
          </bk-tag>
        </template>
      </bk-table-column>
      <bk-table-column prop="createdAt" label="创建时间" width="180" sortable />
      <bk-table-column label="操作" width="180" fixed="right">
        <template slot-scope="{ row }">
          <bk-button text theme="primary" @click="handleEdit(row)">编辑</bk-button>
          <bk-popconfirm
            title="确认删除"
            content="此操作不可撤销"
            @confirm="handleDelete(row)"
          >
            <bk-button text theme="danger">删除</bk-button>
          </bk-popconfirm>
        </template>
      </bk-table-column>
    </bk-table>
    
    <!-- 分页 -->
    <bk-pagination
      :current.sync="pagination.current"
      :count="pagination.count"
      :limit.sync="pagination.limit"
      @change="handlePageChange"
      @limit-change="handleLimitChange"
    />
    
    <!-- 编辑对话框 -->
    <bk-dialog
      v-model="editDialog.visible"
      :title="editDialog.isEdit ? '编辑' : '新增'"
      :confirm-fn="handleSave"
      width="600"
    >
      <bk-form :model="editDialog.form" :rules="editRules" ref="editForm" label-width="100">
        <bk-form-item label="名称" property="name" required>
          <bk-input v-model="editDialog.form.name" />
        </bk-form-item>
        <bk-form-item label="状态" property="status">
          <bk-select v-model="editDialog.form.status">
            <bk-option id="active" name="启用" />
            <bk-option id="inactive" name="禁用" />
          </bk-select>
        </bk-form-item>
      </bk-form>
    </bk-dialog>
  </div>
</template>

<script>
export default {
  data() {
    return {
      loading: false,
      tableData: [],
      selectedRows: [],
      pagination: { current: 1, count: 0, limit: 10 },
      editDialog: {
        visible: false,
        isEdit: false,
        form: { name: '', status: 'active' }
      },
      editRules: {
        name: [{ required: true, message: '名称不能为空', trigger: 'blur' }]
      }
    }
  },
  methods: {
    handleSelectionChange(selection) {
      this.selectedRows = selection
    },
    handleCreate() {
      this.editDialog = {
        visible: true,
        isEdit: false,
        form: { name: '', status: 'active' }
      }
    },
    handleEdit(row) {
      this.editDialog = {
        visible: true,
        isEdit: true,
        form: { ...row }
      }
    },
    async handleSave() {
      await this.$refs.editForm.validate()
      // 保存逻辑
      await this.fetchData()
      return true
    },
    async handleDelete(row) {
      await this.deleteItem(row.id)
      this.$bkMessage({ theme: 'success', message: '删除成功' })
      this.fetchData()
    },
    async handleBatchDelete() {
      await this.$bkInfo({
        title: '确认批量删除',
        subTitle: `确定删除 ${this.selectedRows.length} 项？`,
        type: 'warning'
      })
      // 批量删除逻辑
    },
    handlePageChange(page) {
      this.pagination.current = page
      this.fetchData()
    },
    handleLimitChange(limit) {
      this.pagination.limit = limit
      this.pagination.current = 1
      this.fetchData()
    }
  }
}
</script>
```

### 可展开行表格

```vue
<bk-table :data="tableData" row-key="id">
  <bk-table-column type="expand">
    <template slot-scope="{ row }">
      <div class="expand-content">
        <bk-description :column="2">
          <bk-description-item label="描述">{{ row.description }}</bk-description-item>
          <bk-description-item label="详情">{{ row.details }}</bk-description-item>
        </bk-description>
      </div>
    </template>
  </bk-table-column>
  <bk-table-column prop="name" label="名称" />
  <bk-table-column prop="status" label="状态" />
</bk-table>
```

---

## 对话框模式

### 多步骤对话框

```vue
<template>
  <bk-dialog v-model="visible" title="创建向导" width="700" :show-footer="false">
    <bk-steps :steps="steps" :cur-step.sync="currentStep" />
    
    <div class="step-content" style="margin-top: 20px;">
      <!-- 步骤 1 -->
      <div v-show="currentStep === 1">
        <bk-form :model="form" ref="step1Form" label-width="100">
          <bk-form-item label="名称" property="name" required>
            <bk-input v-model="form.name" />
          </bk-form-item>
        </bk-form>
      </div>
      
      <!-- 步骤 2 -->
      <div v-show="currentStep === 2">
        <bk-form :model="form" ref="step2Form" label-width="100">
          <bk-form-item label="配置" property="config">
            <bk-input v-model="form.config" type="textarea" :rows="4" />
          </bk-form-item>
        </bk-form>
      </div>
      
      <!-- 步骤 3：确认 -->
      <div v-show="currentStep === 3">
        <bk-description>
          <bk-description-item label="名称">{{ form.name }}</bk-description-item>
          <bk-description-item label="配置">{{ form.config }}</bk-description-item>
        </bk-description>
      </div>
    </div>
    
    <div class="dialog-footer" style="margin-top: 20px; text-align: right;">
      <bk-button v-if="currentStep > 1" @click="currentStep--">上一步</bk-button>
      <bk-button v-if="currentStep < 3" theme="primary" @click="nextStep">下一步</bk-button>
      <bk-button v-if="currentStep === 3" theme="primary" :loading="submitting" @click="handleSubmit">
        提交
      </bk-button>
    </div>
  </bk-dialog>
</template>

<script>
export default {
  data() {
    return {
      visible: false,
      currentStep: 1,
      steps: [
        { title: '基本信息' },
        { title: '配置项' },
        { title: '确认' }
      ],
      form: { name: '', config: '' },
      submitting: false
    }
  },
  methods: {
    async nextStep() {
      const formRef = this.$refs[`step${this.currentStep}Form`]
      if (formRef) {
        await formRef.validate()
      }
      this.currentStep++
    },
    async handleSubmit() {
      this.submitting = true
      try {
        await this.saveData()
        this.$bkMessage({ theme: 'success', message: '创建成功！' })
        this.visible = false
      } finally {
        this.submitting = false
      }
    }
  }
}
</script>
```

### 带加载的确认框

```vue
<script>
methods: {
  async handleDelete(item) {
    const info = this.$bkInfo({
      title: '确认删除',
      subTitle: `删除 "${item.name}"？`,
      type: 'warning',
      confirmFn: async () => {
        try {
          await this.deleteItem(item.id)
          this.$bkMessage({ theme: 'success', message: '删除成功！' })
          this.fetchData()
        } catch (error) {
          this.$bkMessage({ theme: 'error', message: error.message })
          throw error // 抛出错误保持对话框打开
        }
      }
    })
  }
}
</script>
```

---

## 导航模式

### 应用布局

```vue
<template>
  <bk-navigation
    :nav-width="260"
    :default-open="true"
    side-title="我的应用"
  >
    <template slot="side-icon">
      <img src="/logo.svg" width="28" />
    </template>
    
    <template slot="header">
      <div class="header-content">
        <bk-breadcrumb separator="/">
          <bk-breadcrumb-item :to="{ path: '/' }">首页</bk-breadcrumb-item>
          <bk-breadcrumb-item>{{ currentRouteName }}</bk-breadcrumb-item>
        </bk-breadcrumb>
        
        <div class="header-right">
          <bk-dropdown-menu>
            <template slot="dropdown-trigger">
              <span class="user-info">
                <i class="bk-icon icon-user"></i>
                {{ username }}
              </span>
            </template>
            <template slot="dropdown-content">
              <ul class="bk-dropdown-list">
                <li @click="goProfile">个人中心</li>
                <li @click="logout">退出登录</li>
              </ul>
            </template>
          </bk-dropdown-menu>
        </div>
      </div>
    </template>
    
    <template slot="menu">
      <bk-navigation-menu :default-active="activeMenu" @select="handleMenuSelect">
        <bk-navigation-menu-item id="dashboard" icon="icon-dashboard">
          仪表盘
        </bk-navigation-menu-item>
        
        <bk-navigation-menu-group name="管理" icon="icon-cog">
          <bk-navigation-menu-item id="users">用户管理</bk-navigation-menu-item>
          <bk-navigation-menu-item id="roles">角色管理</bk-navigation-menu-item>
        </bk-navigation-menu-group>
        
        <bk-navigation-menu-group name="设置" icon="icon-cog-shape">
          <bk-navigation-menu-item id="general">常规设置</bk-navigation-menu-item>
          <bk-navigation-menu-item id="advanced">高级设置</bk-navigation-menu-item>
        </bk-navigation-menu-group>
      </bk-navigation-menu>
    </template>
    
    <div class="main-content">
      <router-view />
    </div>
  </bk-navigation>
</template>
```

### 标签页内容

```vue
<template>
  <div class="tab-container">
    <bk-tab :active.sync="activeTab" type="card" closable addable @add-panel="handleAdd" @close-panel="handleClose">
      <bk-tab-panel
        v-for="tab in tabs"
        :key="tab.name"
        :name="tab.name"
        :label="tab.label"
        :closable="tabs.length > 1"
      >
        <component :is="tab.component" v-bind="tab.props" />
      </bk-tab-panel>
    </bk-tab>
  </div>
</template>

<script>
export default {
  data() {
    return {
      activeTab: 'tab1',
      tabs: [
        { name: 'tab1', label: '标签 1', component: 'ContentComponent', props: { id: 1 } }
      ],
      tabCounter: 1
    }
  },
  methods: {
    handleAdd() {
      this.tabCounter++
      const newTab = {
        name: `tab${this.tabCounter}`,
        label: `标签 ${this.tabCounter}`,
        component: 'ContentComponent',
        props: { id: this.tabCounter }
      }
      this.tabs.push(newTab)
      this.activeTab = newTab.name
    },
    handleClose(name) {
      const index = this.tabs.findIndex(tab => tab.name === name)
      this.tabs.splice(index, 1)
      if (this.activeTab === name) {
        this.activeTab = this.tabs[Math.max(0, index - 1)]?.name
      }
    }
  }
}
</script>
```

---

## 加载模式

### 页面加载与骨架屏

```vue
<template>
  <div class="page-container">
    <div v-if="loading" class="skeleton-wrapper">
      <!-- 骨架屏内容 -->
      <div class="skeleton-header"></div>
      <div class="skeleton-content"></div>
    </div>
    
    <template v-else-if="data">
      <!-- 实际内容 -->
      <div class="page-content">
        {{ data }}
      </div>
    </template>
    
    <bk-exception v-else type="empty">
      暂无数据
    </bk-exception>
  </div>
</template>
```

### 按钮加载状态

```vue
<bk-button
  theme="primary"
  :loading="saving"
  :disabled="!canSave"
  @click="handleSave"
>
  {{ saving ? '保存中...' : '保存' }}
</bk-button>
```

### 异步操作加载

```vue
<script>
methods: {
  async handleOperation() {
    const loading = this.$bkLoading({ title: '处理中...' })
    try {
      await this.doSomething()
      this.$bkMessage({ theme: 'success', message: '完成！' })
    } catch (error) {
      this.$bkMessage({ theme: 'error', message: error.message })
    } finally {
      loading.hide()
    }
  }
}
</script>
```

---

## 树形模式

### 带右键菜单的树

```vue
<template>
  <bk-tree
    :data="treeData"
    node-key="id"
    @node-contextmenu="handleContextMenu"
  >
    <template slot-scope="{ data }">
      <span>{{ data.name }}</span>
    </template>
  </bk-tree>
  
  <div
    v-if="contextMenu.visible"
    v-bk-clickoutside="closeContextMenu"
    class="context-menu"
    :style="{ top: contextMenu.y + 'px', left: contextMenu.x + 'px' }"
  >
    <ul>
      <li @click="handleAddChild">添加子节点</li>
      <li @click="handleRename">重命名</li>
      <li @click="handleDelete">删除</li>
    </ul>
  </div>
</template>
```

### 懒加载树

```vue
<bk-tree
  :data="treeData"
  node-key="id"
  lazy
  :load="loadChildren"
  :props="{ label: 'name', children: 'children', isLeaf: 'isLeaf' }"
/>

<script>
methods: {
  async loadChildren(node, resolve) {
    if (node.level === 0) {
      return resolve(this.rootNodes)
    }
    const children = await this.fetchChildren(node.data.id)
    resolve(children)
  }
}
</script>
```

---

## 搜索模式

### 防抖搜索

```vue
<template>
  <bk-input
    v-model="searchKeyword"
    placeholder="搜索..."
    clearable
    @input="debouncedSearch"
  />
</template>

<script>
import { debounce } from 'lodash'

export default {
  data() {
    return {
      searchKeyword: ''
    }
  },
  created() {
    this.debouncedSearch = debounce(this.handleSearch, 300)
  },
  methods: {
    handleSearch() {
      this.fetchData({ keyword: this.searchKeyword })
    }
  }
}
</script>
```

### 高级搜索 SearchSelect

```vue
<bk-search-select
  :data="searchConditions"
  :values="searchValues"
  @change="handleSearchChange"
/>

<script>
export default {
  data() {
    return {
      searchConditions: [
        {
          id: 'status',
          name: '状态',
          multiable: true,
          children: [
            { id: 'active', name: '启用' },
            { id: 'inactive', name: '禁用' }
          ]
        },
        {
          id: 'name',
          name: '名称'
        },
        {
          id: 'createdAt',
          name: '创建日期',
          children: [
            { id: 'today', name: '今天' },
            { id: 'week', name: '本周' },
            { id: 'month', name: '本月' }
          ]
        }
      ],
      searchValues: []
    }
  },
  methods: {
    handleSearchChange(values) {
      this.searchValues = values
      const params = this.buildSearchParams(values)
      this.fetchData(params)
    }
  }
}
</script>
```
