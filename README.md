Scripts to interact with PCF opsmanager. 

Specifically at this point to grab credentials and look at json output for tiles that are installed. Mainly useful for automation
pipelines. 

#Example get tile json

    getprodstg
    0 - p-bosh-3ba3fd4832b4a752bca0
    1 - apm-fc14171bd23113f48edf
    2 - p-redis-efb047ee04802cf2b763
    3 - p-metrics-789beff8c4151c38141a
    4 - p-rabbitmq-e0a50d17bbb3e7c95389
    5 - cf-ed94e9133df42fc146ab
    6 - p-mysql-03d1ee28b6a573599a4f
    choose product you want to review from above list starting at 0: 6
    0 - resources
    1 - properties
    2 - networks_and_azs
    choose endpoint to investigate [resouce properties networks_and_azs] starting at 0 : 0
    p-mysql-03d1ee28b6a573599a4f
    {
      "resources": [
        {
          "identifier": "mysql",
          "description": "",
          "instances": 3,
          "instances_best_fit": 3,
          "instance_type_id": "",
          "instance_type_best_fit": "large.disk",
          "persistent_disk_mb": 102400,
          "persistent_disk_best_fit": 100000
        },
        {
          "identifier": "backup-prepare",
          "description": "",
          "instances": 1,
          "instances_best_fit": 0,
          "instance_type_id": "",
          "instance_type_best_fit": "micro.ram",
          "persistent_disk_mb": 204800,
          "persistent_disk_best_fit": 200000
        },
        {
          "identifier": "proxy",
          "description": "",
          "instances": 2,
          "instances_best_fit": 2,
          "instance_type_id": "",
          "instance_type_best_fit": "small.disk"
        },
        {
          "identifier": "monitoring",
          "description": "",
          "instances": 1,
          "instances_best_fit": 1,
          "instance_type_id": "",
          "instance_type_best_fit": "micro"
        },
        {
          "identifier": "cf-mysql-broker",
          "description": "",
          "instances": 2,
          "instances_best_fit": 2,
          "instance_type_id": "",
          "instance_type_best_fit": "small.disk"
        },
        {
          "identifier": "broker-registrar",
          "description": "",
          "instances": "",
          "instances_best_fit": 1,
          "instance_type_id": "",
          "instance_type_best_fit": "small"
        },
        {
          "identifier": "deregister-and-purge-instances",
          "description": "",
          "instances": "",
          "instances_best_fit": 1,
          "instance_type_id": "",
          "instance_type_best_fit": "small"
        },
        {
          "identifier": "rejoin-unsafe",
          "description": "",
          "instances": "",
          "instances_best_fit": 1,
          "instance_type_id": "",
          "instance_type_best_fit": "micro"
        },
        {
          "identifier": "smoke-tests",
          "description": "",
          "instances": "",
          "instances_best_fit": 1,
          "instance_type_id": "",
          "instance_type_best_fit": "small"
        },
        {
          "identifier": "bootstrap",
          "description": "",
          "instances": "",
          "instances_best_fit": 1,
          "instance_type_id": "",
          "instance_type_best_fit": "small"
        }
      ]
    }
    
#Example get creds

    [user@ scripts]$ creds
   
     director
     e_HOxWIe9q51aHTGKGg3lb_tUbSJ_3jw
