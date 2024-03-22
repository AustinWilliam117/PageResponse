This is a test case for a page request to return response time.

```yaml
- name: 通话明细默认查询
  base_url: 'http://10.54.0.30:19048/pbot/audio/iod/report/'
  request:
  method: 'GET'
  request_url: 'call_list'
  params:   
    conditions:
      call_time_start: '2024-03-15 00:00:00'
      call_time_end: '2024-03-15 23:59:59'
      call_id: ''
      caller: ''
      duration_start: ''    # -> int, 通话起止时间
      duration_end: ''  # -> int, 通话起止时间
      roboot_flow: ''
      robootId: ''
      entrance_id: ''   # -> str, 项目ID
      disconnect_reason: '' # -> int(0/1/2/3/4/5/6), 挂机原因，不传查全部
      task_id: ''  # -> str, 在线ID
      business_success: ''  # -> int(1/0), 任务是否完成，1完成，0未完成
    page_size: '20'   # -> int(5/10/20/50), 返回条数
    call_label: ''    # -> str, 意向标签
    date_start: '202403'
    date_end: '202403'
    flip: ''  # -> str(down/up), 翻页动作，有值时chiasm为空字符串
    min_id: '0'
    max_id: '0'
    chiasm: 'home'
  validate:
    - eq:
        - msg
        - '数据库查询成功'

```