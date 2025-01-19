# Flask 用户认证系统

这是一个基于 Flask 的简单用户认证系统，实现了用户注册和登录功能。

## 功能特性

- 用户注册
- 用户登录
- 用户登出
- MySQL 数据库集成
- 密码加密存储
- 用户会话管理

## 技术栈

- Python 3.8+
- Flask 2.3.3
- MySQL 5.7+
- Flask-SQLAlchemy
- Flask-Login
- PyMySQL

## 安装步骤

1. 克隆项目
```bash
git clone [你的项目地址]
cd [项目目录]
```

2. 创建并激活虚拟环境
```bash
# 创建虚拟环境
python -m venv venv

# 在 Linux/Mac 上激活虚拟环境
source venv/bin/activate

# 在 Windows 上激活虚拟环境
venv\Scripts\activate
```

3. 安装依赖
```bash
pip install -r requirements.txt
```

4. 配置数据库
- 在 MySQL 中创建新数据库
```sql
CREATE DATABASE your_database_name;
```
- 修改 `app.py` 中的数据库配置
```python
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://username:password@localhost/dbname'
```
将 username、password 和 dbname 替换为你的实际数据库信息。

5. 初始化数据库
```bash
# 启动 Python 交互式环境
python
```
```python
from app import db
db.create_all()
exit()
```

## 运行项目

```bash
python app.py
```

访问 http://127.0.0.1:5000 即可看到应用首页。

## 项目结构

```
.
├── README.md
├── requirements.txt
├── app.py                 # 主应用文件
└── templates/            # HTML 模板目录
    ├── index.html       # 首页模板
    ├── login.html      # 登录页面模板
    └── register.html   # 注册页面模板
```

## 环境要求

- Python 3.8 或更高版本
- MySQL 5.7 或更高版本
- pip 包管理器

## 配置说明

主要配置项在 `app.py` 中：

- `SECRET_KEY`：用于会话加密，生产环境中应使用强密钥
- `SQLALCHEMY_DATABASE_URI`：数据库连接配置
- `SQLALCHEMY_TRACK_MODIFICATIONS`：是否追踪数据库修改

## 开发说明

1. 数据模型在 `app.py` 中的 `User` 类定义
2. 所有路由处理器都在 `app.py` 中
3. 前端模板存放在 `templates` 目录下

## 安全注意事项

1. 在生产环境中，请修改 `SECRET_KEY`
2. 确保数据库密码安全存储
3. 建议使用环境变量存储敏感信息

## 贡献指南

1. Fork 本项目
2. 创建你的特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交你的改动 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 创建一个 Pull Request

## 许可证

[选择合适的开源许可证，例如 MIT License]

## 联系方式

[你的联系方式或者项目讨论区链接]
