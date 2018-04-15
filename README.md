# fastnetmon_web-hook-receiver
Get fastnetmon advanced web-hook json

#### check with curl

```
curl -H "Content-Type: application/json" -X POST -d '{"flow_spec_rules": [ { "source_prefix": "10.10.193.154/32", "destination_ports": [ 80 ], "source_ports": [ 62586 ], "packet_lengths": [ 40 ], "protocols": [ "tcp" ], "tcp_flags": [ "syn" ], "action_type": "discard", "action": { } } ]}' http://10.10.202.200:8088
```
