# -*- coding: utf-8 -*-
# @File  : configs.py
# @Date  : 2019/1/11
# @Desc  :
import os

from django.conf import settings

CODE_MSG = {
    200: '服务器成功返回请求的数据',
    201: '新建或修改数据成功',
    202: '一个请求已经进入后台排队（异步任务）',
    204: '删除数据成功',
    400: '发出的请求有错误，服务器没有进行新建或修改数据的操作',
    401: '用户没有权限（令牌、用户名、密码错误）',
    403: '用户得到授权，但是访问是被禁止的',
    404: '发出的请求针对的是不存在的记录，服务器没有进行操作',
    405: '发送的新建请求失败,返回空数据',
    406: '请求的格式不可得',
    409: '请求的资源存在异常',
    410: '请求的资源被永久删除，且不会再得到的',
    422: '当创建一个对象时，发生一个验证错误',
    500: '服务器发生错误，请检查服务器',
    502: '网关错误',
    503: '服务不可用，服务器暂时过载或维护',
    504: '网关超时',
    505: "MSFRPC调用失败",
    # 自定义的错误码
    408: '填写的端口已占用',
}

BASEAUTH_MSG = {
    201: '登录成功',


    301: '登录失败,密码错误',

}
PORTFWD_MSG = {
    201: '新建端口转发成功',
    204: '删除端口转发成功',

    301: '无法创建转发,请确认服务器及目标主机端口未占用',
    302: '解析运行结果失败',
    305: '删除端口转发失败',
    306: '参数检查失败',
    307: '删除端口转发失败',
    308: 'MSFRPC调用失败',
}

TRANSPORT_MSG = {
    201: "新增传输成功",
    202: "切换传输成功",
    203: "休眠命令发送成功",
    204: "删除传输成功",
    205: "",
    206: "",

    301: '添加传输失败,请选择其他监听',
    302: '切换传输失败',
    303: '无法解析所选监听参数,请选择其他监听',
    304: '删除传输失败',
    305: '休眠Session失败',
    306: '输入参数错误',
}

PostModuleActuator_MSG = {
    201: "新建后台任务成功",
    202: "",
    203: "",
    204: "",
    205: "",
    206: "",

    301: "模块前序检查失败,检查函数内部错误",
    302: "",
    303: "",
    304: "",
    305: "获取模块配置失败",
    306: "新建后台任务失败",

}

PostModuleConfig_MSG = {
    201: "更新模块配置成功",
    202: "",
    203: "",
    204: "",
    205: "",
    206: "",

    301: "",
    302: "",
    303: "",
    304: "",
    305: "",
    306: "",
}

PostModuleResultHistory_MSG = {
    201: "",
    202: "",
    203: "",
    204: "删除历史记录成功",
    205: "",
    206: "",

    301: "",
    302: "",
    303: "",
    304: "输入参数错误",
    305: "",
    306: "",
}

Setting_MSG = {
    201: "获取chat_id列表成功",
    202: "设置Telegram通知成功",
    203: "设置DingDing通知成功",
    204: "设置Session监控成功",
    205: "设置回连地址成功",
    206: "设置FOFA API成功",

    301: "未知配置类型",
    302: "解析配置参数失败",
    303: "输入的Telegram配置不可用,请检查token是否正确且网络可以访问telegram",
    304: "输入的DingDing配置不可用,请检查token是否正确且安全关键字是否正确",
    306: "输入的FOFA配置不可用,请检查email及key是否正确",
}

NetworkSearch_MSG = {
    201: "查询数据成功",
    202: "",
    203: "",
    204: "",
    205: "",

    301: "API接口调用失败,请确认FOFA等配置是否正确",
    302: "",
    303: "查询接口异常",
    304: "无效的搜索引擎",
}

Host_MSG = {
    201: "更新主机标签成功",
    202: "删除主机成功",
    203: "",
    204: "",
    205: "",
    206: "",

    301: "删除主机失败,该主机不存在",
    302: "",
    303: "",
    304: "主机不存在",
    305: "",
    306: "",
}

HostFile_MSG = {
    201: "",
    202: "",
    203: "",
    204: "",
    205: "",
    206: "",

    301: "",
    302: "",
    303: "",
    304: "请求文件不存在",
    305: "",
    306: "",
}
Session_MSG = {
    201: "删除权限成功",
    202: "删除权限命令已发送",
    203: "更新Session信息成功",
    204: "",
    205: "",
    206: "",

    301: "删除权限异常",
    302: "",
    303: "",
    304: "输入参数错误",
    305: "",
    306: "",
}
SessionIO_MSG = {
    200: "发送命令成功",
    201: "发送命令成功",
    202: "读取结果成功",
    203: "退出Session",
    204: "清空历史记录成功",
    205: "",
    206: "",

    301: "",
    302: "",
    303: "执行操作超时",
    304: "",
    305: "发送命令失败",
    306: "系统内部异常",
}

Socks_MSG = {
    201: "新建socks代理成功",
    202: "",
    203: "",
    204: "删除socks代理成功",
    205: "",
    206: "",

    301: "",
    302: "",
    303: "执行操作超时",
    304: "输入参数错误",
    305: "解析配置参数失败",
    306: "新建socks代理失败",
}

Notice_MSG = {
    200: "发送消息成功",
    201: "清除通知成功",
    202: "发送消息成功",
    203: "",
    204: "",
    205: "",
    206: "",

    301: "",
    302: "",
    303: "",
    304: "",
    305: "",
    306: "",
}

FileMsf_MSG = {
    201: "上传文件成功",
    202: "删除文件成功",
    203: "下载文件成功",
    204: "",
    205: "",
    206: "",

    301: "文件不存在",
    302: "上传文件失败",
    303: "下载文件失败",
    304: "",
    305: "",
    306: "",
}

FileSession_MSG = {
    201: "执行操作成功",
    202: "后台执行成功",
    203: "切换工作目录成功",
    204: "更新文件内容成功",
    205: "",
    206: "",

    301: "执行操作超时",
    302: "解析结果异常",
    303: "执行操作失败",
    304: "",
    305: "",
    306: "未知命令",
}

Handler_MSG = {
    201: "新建监听成功",
    202: "删除监听成功",
    203: "",
    204: "",
    205: "",
    206: "",

    301: "新建监听超时",
    302: "新建监听失败",
    303: "输入参数错误",
    304: "",
    305: "",
    306: "端口已占用",
}

Job_MSG = {
    201: "",
    202: "",
    203: "",
    204: "删除任务成功",
    205: "",
    206: "",

    301: "后台任务不存在",
    302: "",
    303: "",
    304: "后台任务不存在",
    305: "删除任务失败",
    306: "",
}

Payload_MSG = {
    201: "生成载荷成功",
    202: "",
    203: "",
    204: "",
    205: "",
    206: "",

    301: "",
    302: "",
    303: "",
    304: "",
    305: "生成载荷失败",
    306: "multi类型监听无法自动生成载荷",
}

Route_MSG = {
    201: "新增路由成功",
    202: "",
    203: "",
    204: "删除路由成功",
    205: "",
    206: "",

    301: "",
    302: "",
    303: "",
    304: "删除路由失败",
    305: "新增路由失败",
    306: "解析结果失败",
    307: "MSFRPC调用失败",
}

Credential_MSG = {
    201: "新增凭证成功",
    202: "更新凭证说明成功",
    203: "",
    204: "删除凭证成功",
    205: "",
    206: "",

    301: "",
    302: "",
    303: "",
    304: "输入参数错误",
    305: "",
    306: "",
}
PortService_MSG = {
    201: "",
    202: "",
    203: "",
    204: "删除端口信息成功",
    205: "",
    206: "",

    301: "",
    302: "",
    303: "",
    304: "输入参数错误",
    305: "",
    306: "",
}

Vulnerability_MSG = {
    201: "",
    202: "",
    203: "",
    204: "删除漏洞信息成功",
    205: "",
    206: "",

    301: "",
    302: "",
    303: "",
    304: "输入参数错误",
    305: "",
    306: "",
}

LazyLoader_MSG = {
    201: "更新配置成功",
    202: "删除配置成功",
    203: "正在下载示例代码",
    204: "",
    205: "",
    206: "",

    301: "",
    302: "",
    303: "解析参数失败",
    304: "未找到对应数据",
    305: "",
    306: "",
}

Empty_MSG = {
    201: "",
    202: "",
    203: "",
    204: "",
    205: "",
    206: "",

    301: "",
    302: "",
    303: "",
    304: "",
    305: "",
    306: "",
}

# token超时时间
EXPIRE_MINUTES = 24 * 60

# 静态配置信息
MSF_RPC_RESULT_CHANNEL = "MSF_RPC_RESULT_CHANNEL"
MSF_RPC_DATA_CHANNEL = "MSF_RPC_DATA_CHANNEL"
MSF_RPC_LOG_CHANNEL = "MSF_RPC_LOG_CHANNEL"
MSF_RPC_CONSOLE_CHANNEL = "MSF_RPC_CONSOLE_CHANNEL"

PAYLOAD_LOADER_STORE_PATH = "STATICFILES/STATIC/SHELLCODELOADER/"

# 静态文件目录
STATIC_STORE_PATH = "STATICFILES/STATIC/"

# 临时目录
TMP_DIR = os.path.join(settings.BASE_DIR, 'STATICFILES', 'TMP')

# meterpreter prompt
METERPRETER_PROMPT = "meterpreter > "
SHELL_PROMPT = "shell > "
