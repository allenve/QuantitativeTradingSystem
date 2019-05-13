## 量化交易管理系统

### start (服务端)
- Django < 2.2(建议版本2.1.4)

- 依赖安装

  ```shell
  pip install django==2.1.4
  pip install pymysql
  pip install pandas_datareader
  pip install tushare
  pip install ta-lib

  pip install mpl_finance 
  ```

- 初始化数据库

  ```shell
  python manage.py makemigrations Quantitative
  ```

  