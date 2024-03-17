from rediscluster import RedisCluster

def return_rediskey(*args):
    """
    连接redis集群，并返回一个PBOT_PHX_4_3为开头的key，用于页面查询
    :return: 一个以PBOT_PHX_4_3为开头的key，如：PBOT_PHX_4_3:979746ea-b1f6-4c1a-a2ff-a6692c4305f6
    """

    # Redis 集群节点
    startup_nodes = [
        {"host": "10.54.0.30", "port": "7000"},
        {"host": "10.54.0.30", "port": "7001"},
        {"host": "10.54.0.30", "port": "7002"},
        {"host": "10.54.0.30", "port": "7003"},
        {"host": "10.54.0.30", "port": "7004"},
        {"host": "10.54.0.30", "port": "7005"},
    ]

    # 创建RedisCluster对象
    """
        decode_responses=True参数表示从Redis集群获取的值应该被自动解码为字符串。
        如果不设置这个参数或设置为False，则获取的值将是bytes类型。
    """
    try:
        # 创建RedisCluster对象
        rc = RedisCluster(startup_nodes=startup_nodes, decode_responses=True, password='Pachira@123')
        # 使用RedisCluster对象执行命令
        for key in rc.keys('*'):
            if key.startswith(args):
                return key
    except Exception as e:
        print(f"redis连接错误，原因为：{e}")

if __name__ == '__main__':
    print(return_rediskey("PBOT_PHX_4_3"))