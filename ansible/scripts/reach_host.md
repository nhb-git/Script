# reach_host.sh用法说明

## shell示例

```playbook
- name: run reach_host.sh script
  script: scripts/reach_host.sh www.baidu.com 80 5

# 或者

- name: check if reach host port
  reach_host: host=www.baidu.com port=80 timeout=5  
```
