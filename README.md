# QMatch
QMatch 是一个用于腾讯会议快速校对当前在会议室的成员的小程序  
您可以下载dist中的已编译版本使用  
  
## 食用方法  
Step1：将名单/花名册放入程序同一路径的data.txt下，一行为一项  
Step2：下载参会人员名单  
Step3：在资源管理器中选中下载的xlsx文件，然后点击上方主页》剪贴板中的复制路径  
Step4：在命令提示符中右击来粘贴路径并回车执行  
Step5：程序会返回不在当前会议室的人员  
  
***复制结果：左键拖选后右击，所拖选的文本便会进入剪贴板***  
  
腾讯会议导出的参会人员名单**有一定延时**，请注意  
__________  
查询当前在会议室的人员原理：  
在导出的xlsx文件中，第二张工作表记录了参会人员的进出会明细，当人员在会内时，离会时间为“--”，藉此来判断人员是否在会议中。  
  
计划中的优化  
[ ]更美观的输出  
[ ]输出数据自动推送到剪贴板  
