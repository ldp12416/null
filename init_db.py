from app import db, app, User

def init_database():
    with app.app_context():
        # 创建所有数据库表
        db.create_all()
        
        # 检查是否已存在管理员用户
        admin_user = User.query.filter_by(username='admin').first()
        if not admin_user:
            # 创建一个管理员用户
            admin = User(username='admin')
            admin.set_password('admin123')  # 在生产环境中使用更强的密码
            db.session.add(admin)
            
            try:
                db.session.commit()
                print("管理员用户创建成功！")
            except Exception as e:
                db.session.rollback()
                print(f"创建管理员用户失败：{str(e)}")
        
        print("数据库初始化完成！")

if __name__ == "__main__":
    init_database() 