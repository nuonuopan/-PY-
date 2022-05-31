
- [x] 在spyder中matplotlib输出位置被修改
    - [参考](https://blog.csdn.net/a18892061545/article/details/122004704)

    - 解决方式：
    1. 仅解决显示问题
    输入 `%matplotlib inline `
    可以看到`print(matplotlib.get_backend())`恢复初始值
    2. 保存图片输出查看
        ```
        fig=plt.figure()
        fig.add_subplot(111)
        plt.plot(capital_list,color='r')
        plt.title('双均线策略的资金曲线')
        plt.show()
        fig.savefig(r'C:\Users\nuonu\Desktop\a.png')
        ```
    3. 全局重制
        ```
        import matplotlib
        matplotlib.use('module://matplotlib_inline.backend_inline')
        ```










###### 问题
- [ ] 无法在vscode里matplotlib的图像
    - [x] 但可以输出图片去查看


