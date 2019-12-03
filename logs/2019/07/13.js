let data = [
{time: 1563032282623, task: "countdown_timer - visualization", duration: "25m"},
{time: 1563032310734, task: "compare curtime with nexttime", duration: "25m"},
{time: 1563033813325, task: "compare curtime with nexttime", duration: "25m"},
{time: 1563035323464, task: "why isnt todays date working", duration: "25m"},
{time: 1563035958146, task: "idle", duration: "10m"},
{time: 1563036038481, task: "waid", duration: "10m"},
{time: 1563036647914, task: "[idk]", duration: "25m"},
{time: 1563036739137, task: "test", duration: "1m"},
{time: 1563036800771, task: "[idk]", duration: "25m"},
{time: 1563036837248, task: "test", duration: "1m"},
{time: 1563036900387, task: "[idk]", duration: "25m"},
{time: 1563036972635, task: "[idk]", duration: "1m"},
{time: 1563037035521, task: "[no name]", duration: "25m"},
{time: 1563037075992, task: "[no name]", duration: "1m"},
{time: 1563037138905, task: "[no name]", duration: "25m"},
{time: 1563037503853, task: "*", duration: "25m"},
{time: 1563037564027, task: "*", duration: "0m"},
{time: 1563037567439, task: "[no name]", duration: "25m"},
{time: 1563037569681, task: "*", duration: "1m"},
{time: 1563037574209, task: "*", duration: "0m"},
{time: 1563037577665, task: "[no name]", duration: "25m"},
{time: 1563037614747, task: "*", duration: "0.5m"},
{time: 1563037620913, task: "[no name]", duration: "25m"},
{time: 1563037622048, task: "*", duration: "0.5m"},
{time: 1563037626873, task: "[no name]", duration: "25m"},
{time: 1563037632495, task: "*", duration: "0.05m"},
{time: 1563037635793, task: "[no name]", duration: "25m"},
{time: 1563037656042, task: "*", duration: "0.05m"},
{time: 1563037660212, task: "[no name]", duration: "25m"},
{time: 1563037663254, task: "*", duration: "0.05m"},
{time: 1563037666599, task: "[no name]", duration: "25m"},
{time: 1563037711838, task: "*", duration: "0.05m"},
{time: 1563037715159, task: "[no name]", duration: "25m"},
{time: 1563037717117, task: "*", duration: "0.05m"},
{time: 1563037720312, task: "[no name]", duration: "25m"},
{time: 1563039367836, task: "*", duration: "0.05m"},
{time: 1563039370897, task: "[no name]", duration: "25m"},
{time: 1563039410583, task: "*", duration: "0.05m"},
{time: 1563039414606, task: "[no name]", duration: "25m"},
{time: 1563039424488, task: "*", duration: "0.05m"},
{time: 1563039427814, task: "[no name]", duration: "25m"},
{time: 1563039434756, task: "*", duration: "0.05m"},
{time: 1563039438289, task: "[no name]", duration: "25m"},
{time: 1563039452220, task: "*", duration: "0.05m"},
{time: 1563039461942, task: "[no name]", duration: "25m"},
{time: 1563039465712, task: "*", duration: "0.05m"},
{time: 1563039469377, task: "*", duration: "0.05m"},
{time: 1563039477220, task: "[no name]", duration: "25m"},
{time: 1563039493947, task: "*", duration: "0.05m"},
{time: 1563039504086, task: "*", duration: "0.05m"},
{time: 1563039510593, task: "*", duration: "0.05m"},
{time: 1563039514332, task: "test*", duration: "0.05m"},
{time: 1563039531074, task: "[no name]", duration: "25m"},
{time: 1563039532209, task: "test*", duration: "0.05m"},
{time: 1563039554024, task: "[no name]", duration: "25m"},
{time: 1563039555167, task: "test*", duration: "0.05m"},
{time: 1563039572444, task: "[no name]", duration: "25m"},
{time: 1563039573586, task: "test*", duration: "0.05m"},
{time: 1563039582283, task: "test*", duration: "0.05m"},
{time: 1563039592932, task: "[no name]", duration: "25m"},
{time: 1563039618422, task: "test*", duration: "0.05m"},
{time: 1563039621794, task: "[no name]", duration: "25m"},
{time: 1563039647081, task: "hello", duration: "25m"},
{time: 1563039654539, task: "*", duration: "0.05m"},
{time: 1563039658610, task: "[no name]", duration: "25m"},
{time: 1563039662271, task: "*", duration: "0.05m"},
{time: 1563039669970, task: "[no name]", duration: "25m"},
{time: 1563039678766, task: "*", duration: "0.05m"},
{time: 1563039693666, task: "[no name]", duration: "25m"},
{time: 1563039794501, task: "sdf", duration: "25m"},
{time: 1563039799440, task: "[no name]", duration: "1m"},
{time: 1563039804389, task: "*", duration: "0.05m"},
{time: 1563039815082, task: "[no name]", duration: "25m"},
{time: 1563039826366, task: "*", duration: "0.05m"},
{time: 1563039903714, task: "[no name]", duration: "25m"},
{time: 1563039908705, task: "*", duration: "0.05m"},
{time: 1563039916682, task: "[no name]", duration: "25m"},
{time: 1563039927966, task: "*", duration: "0.008m"},
{time: 1563039931336, task: "[no name]", duration: "25m"},
{time: 1563039933735, task: "*", duration: "0m"},
{time: 1563039937002, task: "[no name]", duration: "25m"},
{time: 1563039941951, task: "*", duration: "0m"},
{time: 1563039945943, task: "[no name]", duration: "25m"},
{time: 1563039948355, task: "test", duration: "25m"},
{time: 1563039964776, task: "*", duration: "0m"},
{time: 1563039975548, task: "[no name]", duration: "25m"},
{time: 1563039984271, task: "*", duration: "0m"},
{time: 1563039989116, task: "[no name]", duration: "25m"},
{time: 1563040027238, task: "*", duration: "0m"},
{time: 1563040030338, task: "[no name]", duration: "25m"},
{time: 1563040094695, task: "*", duration: "0m"},
{time: 1563040095824, task: "*", duration: "0m"},
{time: 1563040100688, task: "[no name]", duration: "25m"},
{time: 1563040459235, task: "*", duration: "0m"},
{time: 1563040460370, task: "*", duration: "0m"},
{time: 1563040464707, task: "[no name]", duration: "25m"},
{time: 1563040468421, task: "*", duration: "0m"},
{time: 1563040472278, task: "[no name]", duration: "25m"},
{time: 1563040495241, task: "*", duration: "0m"},
{time: 1563040498818, task: "[no name]", duration: "25m"},
{time: 1563040553322, task: "*", duration: "0m"},
{time: 1563040558560, task: "[no name]", duration: "25m"},
{time: 1563040614858, task: "*", duration: "0m"},
{time: 1563040620977, task: "[no name]", duration: "25m"},
{time: 1563040636258, task: "*", duration: "0m"},
{time: 1563040640987, task: "[no name]", duration: "25m"},
{time: 1563040726649, task: "waid", duration: "10m"},
{time: 1563067690690, task: "idle", duration: "10m"},
]