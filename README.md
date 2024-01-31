# **customized_response**

这是一个依赖python实现的简单http服务端模拟

## **使用方法**
1. 加载镜像
~~~
docker load -i customized_response_2.1.tar
~~~
2. 运行容器
~~~
docker run -p 8888:8888 -d customized_response:2.1
~~~
3. 浏览器访问来配置响应信息
~~~
http://x.x.x.x:8888/api/v1/config
~~~
<div align="center">
  <img src="https://github.com/TomCat552/customized_response/blob/main/images/customized_response_1.png">
</div>
4. 输入对应的响应头和响应体信息，点击更新信息
<div align="center">
  <img src="https://github.com/TomCat552/customized_response/blob/main/images/customized_response_2.png">
</div>
5. 随便访问任意路径（非/api/v1/config路径）
<div align="center">
  <img src="https://github.com/TomCat552/customized_response/blob/main/images/customized_response_3.png">
</div>

### **NOTES**
如果需要修改响应信息，重新访问 http://x.x.x.x:8888/api/v1/config 配置即可
