# scmicropy

## button

| Scratch | Python |
| ------- | ------ |
| <s3b>按键[A v]被按下？</s3b> | gb.button("a") |

## imu

| Scratch | Python |
| ------- | ------ |
| <s3b>加速度[X v]</s3b> | gb.imu.acc("X") |

## pitchroll

| Scratch | Python |
| ------- | ------ |
| <s3b>俯仰角[Pitch v]</s3b> | gb.imu.attitude("pitch") |

## gesture

| Scratch | Python |
| ------- | ------ |
| <s3b>姿态 [摇晃 v]</s3b> | gb.imu.gesture("shake") |

## digitalwrite

| Scratch | Python |
| ------- | ------ |
| <s3b>引脚 序号 [P1 v] 设置电平 (高 v)</s3b> | gb.digiWrite("p1",1) |

## analogwrite

| Scratch | Python |
| ------- | ------ |
| <s3b>引脚 序号[P1 v]写模拟值[150]</s3b> | gb.pwm("p1",150) |

## digitalread

| Scratch | Python |
| ------- | ------ |
| <s3b>引脚 序号[P1 v] 高电平？</s3b> | gb.digiRead("p1") |

## touchread

| Scratch | Python |
| ------- | ------ |
| <s3b>引脚 序号[P1 v] 被触摸？</s3b> | gb.touch("p1") > 100 |

## analogread

| Scratch | Python |
| ------- | ------ |
| <s3b>引脚 序号[P1 v] 模拟值</s3b> | gb.analogread("p1") |

## pixel

| Scratch | Python |
| ------- | ------ |
| <s3b>彩灯[#FF8000] [#FF8000] [#FF8000] [#FF8000]</s3b> | gb.setRGB(#FF8000,#FF8000,#FF8000,#FF8000) |

## pixeltonum

| Scratch | Python |
| ------- | ------ |
| <s3b>彩灯 序号(2 v) 颜色[#FF8000]</s3b> | gb.setRGBN(1,#FF8000) |

## pixelall

| Scratch | Python |
| ------- | ------ |
| <s3b>彩灯 所有颜色[#FF8000]</s3b> | gb.setRGBAll(#FF8000) |

## pixleallrgb

| Scratch | Python |
| ------- | ------ |
| <s3b>彩灯 所有颜色 R(255) G(128) B(0)</s3b> | gb.setRGBAll((255,128,0)) |

## pixelclear

| Scratch | Python |
| ------- | ------ |
| <s3b>彩灯 熄灭所有灯</s3b> | gb.setRGBAll((0,0,0)) |

## motor

| Scratch | Python |
| ------- | ------ |
| <s3b>电机 序号[1 v] 速度[50]%</s3b> | gb.motor(1, 50) |

## motorDual

| Scratch | Python |
| ------- | ------ |
| <s3b>电机 序号1[50]% 序号2[50]%</s3b> | gb.motorDual(50, 50) |

## buzz

| Scratch | Python |
| ------- | ------ |
| <s3b>蜂鸣器 频率(200)延时(1)秒</s3b> | gb.buzz.tone(200,1) |

## buzzcontinueplay

| Scratch | Python |
| ------- | ------ |
| <s3b>蜂鸣器 持续播放 频率(200)</s3b> | gb.buzz.tone(200, -1) |

## music

| Scratch | Python |
| ------- | ------ |
| <s3b>蜂鸣器旋律[r4:2 g g g eb:8 r:2 f f f d:8 ]</s3b> | gb.buzz.melody("r4:2 g g g eb:8 r:2 f f f d:8 ") |

## melody

| Scratch | Python |
| ------- | ------ |
| <s3b>蜂鸣器旋律[CORRECT v]</s3b> | gb.buzz.melody(1) |

## buzzstop

| Scratch | Python |
| ------- | ------ |
| <s3b>蜂鸣器 停止播放</s3b> | gb.buzz.stop() |

## radio_channel

| Scratch | Python |
| ------- | ------ |
| <s3b>设置 无线频道[1]</s3b> | radio.channel = 1 |

## redio_read

| Scratch | Python |
| ------- | ------ |
| <s3b>无线 接收消息</s3b> | radio.read() |

## radio_readtimeout

| Scratch | Python |
| ------- | ------ |
| <s3b>无线 等待消息 超时(5000)毫秒</s3b> | radio.read(timeout=5000) |

## radio_send

| Scratch | Python |
| ------- | ------ |
| <s3b>无线 发送消息[hello]</s3b> | radio.send("hello") |

## wifi

| Scratch | Python |
| ------- | ------ |
| <s3b>连接WIFI[Kittenbot] 密码[123123]</s3b> | gb.wifi.connect("Kittenbot","123123") |

## ipaddr

| Scratch | Python |
| ------- | ------ |
| <s3b>获取WIFI IP</s3b> | gb.wifi.ipaddr() |

## mqttconnect

| Scratch | Python |
| ------- | ------ |
| <s3b>连接小喵MQTT服务器</s3b> | gb.wifi.mqttConnect() |

## mqttconnectserver

| Scratch | Python |
| ------- | ------ |
| <s3b>连接MQTT服务器 [iot.kittenbot.cn] id[ClientId] 用户名[] 密码[]</s3b> | gb.wifi.mqttConnect(host="iot.kittenbot.cn", port=1883, id="ClientId" ,user="", password="") |

## mqttsub

| Scratch | Python |
| ------- | ------ |
| <s3b>订阅MQTT话题[topic1]</s3b> | gb.wifi.mqttSub("topic1") |

## mqttpub

| Scratch | Python |
| ------- | ------ |
| <s3b>向MQTT话题[topic1] 发布消息[helloworld]</s3b> | gb.wifi.mqttPub("topic1", "helloworld") |

## mqttread

| Scratch | Python |
| ------- | ------ |
| <s3b>读取MQTT话题消息[topic1]</s3b> | gb.wifi.mqttRead("topic1") |

