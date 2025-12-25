الطريقة 1 (الأفضل): اقفل اللي ماسك المنفذ 6653 ثم شغّل Ryu
1) اعرف مين ماسك 6653:

نفّذي:

sudo lsof -i :6653


أو:

sudo ss -lntp | grep 6653

2) اقفلي العملية اللي طالعة (PID)

إذا ظهر لك PID مثلًا 1234:

sudo kill -9 1234

3) شغّلي Ryu من جديد:
ryu-manager ryu.app.simple_switch_13

✅ الطريقة 2 (الأسرع بدون قتل أي شيء): شغّلي Ryu على منفذ مختلف (مثلاً 6654)

شغّلي:

ryu-manager --ofp-tcp-listen-port 6654 ryu.app.simple_switch_13


بس انتبهي: لازم تغيّري منفذ الكنترولر في سكربتك أيضًا من 6653 إلى 6654:

في الكود عند:

c1 = net.addController('c1', controller=RemoteController, ip='127.0.0.1', port=6653)


خليه:

c1 = net.addController('c1', controller=RemoteController, ip='127.0.0.1', port=6654)

✅ كيف تشغّلي المشروع “بالظبط” بعد الحل
1) افتحي ترمنال 1 وشغّلي Ryu

إذا استخدمتي الطريقة 1:

ryu-manager ryu.app.simple_switch_13


إذا استخدمتي الطريقة 2 (منفذ 6654):

ryu-manager --ofp-tcp-listen-port 6654 ryu.app.simple_switch_13


خليه شغال وما تسكريه.

2) افتحي ترمنال 2 وشغّلي سكربت Mininet-WiFi

روحي لمجلد سكربتك ثم:

sudo python3 mobilityModel.py


(أو اسم ملفك الحقيقي)

3) داخل CLI جرّبي Ping

داخل CLI اكتبي:

sta1 ping -c 4 sta2

4) تأكدي أن ap1 اتصل بـ Ryu

داخل CLI:

ap1 ovs-vsctl show


لازم تلاقي سطر فيه Controller مثل:

tcp:127.0.0.1:6653 أو tcp:127.0.0.1:6654 حسب اختيارك

ولو حابة تشوفي الـ flows:

ap1 ovs-ofctl -O OpenFlow13 dump-flows ap1

لو تبغي حل “مضمون” بدون ما نخمن: نفّذي هذا الآن وانسخي الناتج

نفّذي:

sudo ss -lntp | egrep '6653|6654'
