# SPDX-License-Identifier: GPL-2.0-or-later
"""Simplified Chinese texts of the Uncharted launcher.

The English text is the key: uncharted_i18n.py merges these over the shared table of bbport_lang,
so a text missing here (or left empty) is shown in English instead of breaking the launcher.
Interface texts, the labels of every choice box, the Fixes page and the controller names are all
translated here; only game titles, version numbers and technical option names are kept in English.
"""

ZH_TRANSLATIONS = {
    # ---- navigation, pages and the brand panel ------------------------------------------------
    'Play': '开始游戏',
    'Game': '游戏',
    'Display': '显示',
    'Controls': '操作',
    'Fixes': '修复',
    'Trophies': '奖杯',
    'Cheats': '作弊',
    'Advanced': '高级',
    'Log': '日志',
    'by {}': '作者：{}',
    'version': '版本',
    'version {}': '版本 {}',
    'Native port: the original PS4 game code runs directly on Windows.':
        '原生移植：PS4 游戏原始代码直接在 Windows 上运行。',
    'Library': '游戏库',
    'Double-click a cover to launch': '双击封面即可启动',
    'Change image': '更换图片',
    'Collection banner': '合集横幅',
    'Set your game folder on the Game page': '请在“游戏”页面设置游戏文件夹',
    'Choose image': '选择图片',
    'Drag an image here or click Choose image.': '把图片拖到这里，或点击“选择图片”。',
    'This image could not be opened: {}': '无法打开此图片：{}',
    'All files': '所有文件',
    'Image files': '图片文件',
    'Horizontal position': '水平位置',
    'Vertical position': '垂直位置',
    'Zoom': '缩放',
    'Restore': '还原',
    'Cancel': '取消',
    'Save changes': '保存更改',
    'Adjust crop': '调整裁剪',

    # ---- Game page ----------------------------------------------------------------------------
    'Your own decrypted dump of the collection (CUSA02343, CUSA02320, …).':
        '你自己解密导出的合集转储（CUSA02343、CUSA02320 …）。',
    'The folder with eboot.bin': '包含 eboot.bin 的文件夹',
    'The folder with eboot.bin, big2-ps4_Shipping.elf and big3-ps4_Shipping.elf. '
    'Leave it empty if every game has a folder of its own, below.':
        '包含 eboot.bin、big2-ps4_Shipping.elf 和 big3-ps4_Shipping.elf 的文件夹。'
        '如果下方每部游戏都有各自的文件夹，请留空。',
    'Separate game folders': '各自的游戏文件夹',
    'Only when the games are not in one collection folder (each dumped on its own). '
    'A game with a folder here is taken from it; the others from the collection folder above.':
        '仅当游戏不在同一个合集文件夹中（各自单独导出）时使用。'
        '此处指定了文件夹的游戏会从该处读取，其余游戏仍读取上面的合集文件夹。',
    'The folder of this game': '此游戏的文件夹',
    'Empty: the collection folder.': '留空：使用合集文件夹。',
    'Where saves and the shader cache are kept': '存档和着色器缓存保存的位置',
    'Empty: the user folder next to the launcher.': '留空：启动器旁边的 user 文件夹。',
    'Console': '主机',
    'Language': '语言',
    'The language the PS4 would be set to; the games use it for text and speech.':
        '相当于 PS4 的系统语言；游戏用它决定文字和语音。',
    'Shown where the game uses the PSN name.': '游戏显示 PSN 名称时使用。',
    'Skip the friends\' stats notice': '跳过好友数据提示',
    'Continue and New Game go straight into the game: the game gets a local player name instead of '
    '\'signed out\' and does not stop on the notice that friends\' stats are not available. '
    'Nothing goes online.':
        '“继续”和“新游戏”会直接进入游戏：游戏会得到一个本地玩家名，而不是显示“已登出”，'
        '也不会停在“好友数据不可用”的提示上。全程不会联网。',

    # ---- Display page -------------------------------------------------------------------------
    'How the game window is shown.': '游戏窗口的显示方式。',
    'Mailbox shows each frame as soon as it is ready without tearing; FIFO waits for the display.':
        'Mailbox 在每帧准备好后立即显示，画面无撕裂；FIFO 会等待显示器刷新。',
    'Gameplay keeps its normal speed at every setting; the cutscene videos always play at 60 FPS. '
    'Above your display\'s refresh rate use Mailbox or Immediate.':
        '无论设置如何，游戏玩法都保持正常速度；过场影片始终以 60 FPS 播放。'
        '超过显示器刷新率时请使用 Mailbox 或 Immediate。',
    'Your display runs at {} Hz.': '你的显示器刷新率为 {} Hz。',
    'Resolution': '分辨率',
    'Render resolution': '渲染分辨率',
    'The size the games draw at, so a 1440p or 4K screen gets a sharper picture, not an enlarged '
    '1080p one. It needs more graphics memory and a faster GPU; the games\' GPU memory limits the '
    'largest size.':
        '游戏实际绘制的尺寸，因此 1440p 或 4K 屏幕能得到更清晰的画面，而不是放大后的 1080p。'
        '需要更多显存和更强的显卡；游戏自身的显存上限决定了最大尺寸。',
    'Aspect ratio': '画面比例',
    'Ultrawide screens: the games draw a wider view (more at the sides) instead of stretching the '
    '16:9 picture. "The shape of the window or screen" follows the window size below, or the '
    'screen in fullscreen.':
        '超宽屏：游戏会绘制更宽的视野（两侧显示更多内容），而不是拉伸 16:9 画面。'
        '“窗口或屏幕的形状”跟随下方的窗口尺寸，全屏时跟随屏幕。',
    'Window size': '窗口尺寸',
    'The window the picture is shown in; fullscreen uses the screen. A picture of another size is '
    'scaled to fit (FSR 1 below when it is enlarged).':
        '画面显示所在的窗口；全屏时使用整个屏幕。其他尺寸的画面会缩放适配'
        '（放大时使用下方的 FSR 1）。',
    'FSR 1 keeps edges sharp when the image is enlarged; bilinear is softer.':
        'FSR 1 在放大画面时保持边缘锐利；双线性更柔和。',
    'Sharpening': '锐化',
    'AMD RCAS after FSR 1 (only while the image is enlarged).':
        '在 FSR 1 之后应用 AMD RCAS（仅在画面放大时）。',
    'Anti-aliasing': '抗锯齿',
    'Temporal anti-aliasing at the games\' 1920 × 1080, with their own motion vectors: smoother '
    'edges and less shimmering than the games\' own. DLSS needs a GeForce RTX; FSR 4 runs best on '
    'a Radeon RX 7000/9000 or a GeForce RTX 40/50. Intel XeSS runs on any GPU (best on Intel Arc).':
        '在游戏原生的 1920 × 1080 下，用游戏自身的运动矢量做时间性抗锯齿：边缘更平滑、闪烁更少，'
        '优于游戏自带抗锯齿。DLSS 需要 GeForce RTX；FSR 4 在 Radeon RX 7000/9000 或 '
        'GeForce RTX 40/50 上效果最佳。Intel XeSS 可用于任何显卡（Intel Arc 上最佳）。',
    'Anti-aliasing sharpness': '抗锯齿锐度',
    'Frame generation': '帧生成',
    'Frames made between two of the game\'s, for smoother motion: 60 FPS shows as 120. Use Mailbox '
    'or Immediate presentation and a display of at least that refresh rate. Adds a little input '
    'latency; menus and cutscene videos are not generated. Use it with the 60 or 120 FPS frame '
    'rate: above about 165 FPS it pauses.':
        '在两帧之间生成中间帧，让运动更平滑：60 FPS 会显示为 120。请使用 Mailbox 或 Immediate '
        '呈现方式，并确保显示器刷新率不低于该值。会略微增加输入延迟；菜单和过场影片不会生成。'
        '请配合 60 或 120 FPS 帧率使用：超过约 165 FPS 时会暂停。',
    'Multiplier': '倍数',
    'FSR 3 makes one frame (2×). DLSS makes up to three on a GeForce RTX 50 (4×), one on an RTX 40.':
        'FSR 3 生成一帧（2×）。DLSS 在 GeForce RTX 50 上最多生成三帧（4×），在 RTX 40 上生成一帧。',
    'Low latency': '低延迟',
    'NVIDIA Reflex on GeForce cards, AMD Anti-Lag 2 on Radeon cards (with a recent driver). The '
    'game waits to read the controller until the GPU is ready for the next frame, so what you '
    'press shows sooner. It helps most when the GPU is the limit; the FPS counter shows it when it '
    'is on.':
        'GeForce 显卡使用 NVIDIA Reflex，Radeon 显卡使用 AMD Anti-Lag 2（需较新驱动）。'
        '游戏会等到 GPU 准备好下一帧时才读取操作，因此按键响应更早。GPU 成为瓶颈时效果最明显；'
        '开启后帧率计数器会显示该状态。',

    # ---- Audio --------------------------------------------------------------------------------
    'Audio': '音频',
    'Speakers': '扬声器',
    'What the games are told the speakers are, which sets the choices in their Audio Output menu '
    '(stereo, 5.1, 7.1). Automatic follows the Windows speaker configuration of the default '
    'playback device; set it to 5.1 or 7.1 when the games only offer stereo.':
        '告知游戏当前的扬声器配置，用于决定其“音频输出”菜单中的选项（立体声、5.1、7.1）。'
        '自动会跟随默认播放设备的 Windows 扬声器配置；如果游戏中只有立体声可选，请设为 5.1 或 7.1。',

    # ---- Controls page ------------------------------------------------------------------------
    'Keyboard, mouse and controller. They work together; changes apply when the game starts.':
        '键盘、鼠标和手柄。它们可同时使用；更改在游戏启动时生效。',
    'Mouse': '鼠标',
    'Look around with the mouse': '用鼠标控制视角',
    'The cursor stays in the game window; hold Left Alt (or switch windows) to free it. '
    'Insert opens the in-game settings menu.':
        '光标会留在游戏窗口内；按住左 Alt（或切换窗口）可释放。按 Insert 打开游戏内设置菜单。',
    'Mouse sensitivity': '鼠标灵敏度',
    'How far the camera turns for a mouse movement; 1.00 is the default. Drag the slider or type a '
    'number (0.1 to 10) for a faster turn.':
        '鼠标移动时镜头转动的幅度；默认 1.00。拖动滑块或直接输入数值（0.1 到 10）可获得更快的转向。',
    'Invert the mouse vertically': '垂直反转鼠标',
    'Button pictures': '按键图标',
    'Show in the game': '游戏中显示',
    'The pictures of buttons in menus and hints. Automatic shows your keys while you use the '
    'keyboard or mouse, Xbox buttons after an Xbox (or other) controller, and the PlayStation '
    'buttons after a PlayStation controller.':
        '菜单和提示中显示的按键图标。自动：使用键盘或鼠标时显示你的按键，连接 Xbox（或其他）手柄'
        '后显示 Xbox 按键，连接 PlayStation 手柄后显示 PlayStation 按键。',
    'Keyboard and mouse buttons': '键盘和鼠标按键',
    'Click a box, then press a key or a mouse button (the wheel counts too). ✕ removes a binding. '
    'Each action can have two.':
        '点击一个方框，然后按一个键或鼠标键（滚轮也算）。✕ 可删除绑定。每个动作可绑定两个。',
    'Default keys': '默认按键',
    'Controller': '手柄',
    'Which controller button gives each PS4 button (Xbox / PlayStation names).':
        '各 PS4 按键对应的手柄按键（Xbox / PlayStation 名称）。',
    'Invert the right stick vertically': '垂直反转右摇杆',
    'Default controller buttons': '默认手柄按键',
    'Vibration': '振动',
    'Detecting…': '正在检测…',
    'Checking vibration support…': '正在检查振动支持…',
    'Status': '状态',
    'Controller vibration': '手柄振动',
    'The setting applies the next time the game starts.': '该设置将在下次游戏启动时生效。',
    'Vibration intensity': '振动强度',
    'Detect controller': '检测手柄',
    'Test vibration': '测试振动',
    'Press a key…': '请按键…',
    'Game controller': '游戏手柄',
    'No controller detected': '未检测到手柄',
    'Connect a controller, then detect again.': '连接手柄后重新检测。',
    'controller probe failed': '手柄检测失败',
    'Could not detect the controller: {}': '无法检测手柄：{}',
    'Connected · Vibration supported': '已连接 · 支持振动',
    'Connected · Vibration not supported': '已连接 · 不支持振动',
    'Connected · Vibration test completed': '已连接 · 振动测试完成',
    'Connected · Vibration test failed': '已连接 · 振动测试失败',
    'Unavailable while the game is running.': '游戏运行期间不可用。',
    'Not available': '不可用',
    'bb-probe.exe was not found.': '找不到 bb-probe.exe。',
    'Testing…': '正在测试…',

    # ---- Fixes page ---------------------------------------------------------------------------
    'Fixes that cost speed. Automatic turns each one on only where it helps; change one only when '
    'you see its problem.':
        '这些修复会降低速度。自动模式只在有帮助的地方开启；只有遇到对应问题时才手动更改。',
    'Exact GPU results (Uncharted 2)': '精确 GPU 结果（神秘海域 2）',
    'Explosions, vehicle damage and the convoy of chapter 21 read results of GPU work back. '
    'Automatic: on in Uncharted 2 only. Costs speed in busy scenes.':
        '爆炸、载具损伤和第 21 章的运输队需要读回 GPU 工作结果。自动：仅在神秘海域 2 中开启。'
        '在复杂场景中会降低速度。',
    'Mesh raycaster copies (Uncharted 2)': '网格射线拾取复制（神秘海域 2）',
    'Fixes "iSubMesh < m_numSubMeshInstances" after checkpoints. Automatic: on in Uncharted 2 only. '
    'In Uncharted 3\'s Cartagena square it cost 94 to 54 FPS.':
        '修复检查点之后出现的 "iSubMesh < m_numSubMeshInstances"。自动：仅在神秘海域 2 中开启。'
        '在神秘海域 3 的卡塔赫纳广场会从 94 FPS 掉到 54 FPS。',
    'Aim and turret focus': '瞄准与炮塔聚焦',
    'Enemies stay in focus when aiming (blurry aim in Uncharted 2 and 3). Automatic: on in '
    'Uncharted 2 and 3, no measurable cost.':
        '瞄准时敌人保持聚焦（修复神秘海域 2、3 中瞄准画面模糊）。自动：在神秘海域 2 和 3 中开启，'
        '无明显性能代价。',
    'Brightness flicker fix': '亮度闪烁修复',
    'Copies small GPU results back every frame (fixes black weapons and stuck brightness). '
    'Automatic: on in Uncharted 2 and 3.':
        '每帧读回较小的 GPU 结果（修复武器变黑和亮度卡住）。自动：在神秘海域 2 和 3 中开启。',
    'Sinking characters fix': '角色下沉修复',
    'Stops characters sinking into the ground, floating or twitching in Uncharted 3. '
    'Automatic: on in Uncharted 3, without FPS cost. On also makes the game wait for these '
    'results every frame: try it if characters still sink, it costs a lot of FPS in heavy scenes.':
        '修复神秘海域 3 中角色陷入地面、悬浮或抽搐的问题。自动：在神秘海域 3 中开启，无帧率代价。'
        '选择“开启”还会让游戏每帧等待这些结果：如果角色仍然下沉可以试试，但在复杂场景中会损失大量帧率。',
    'Small video memory mode': '小显存模式',
    'Keeps 4-8 GB graphics cards inside their video memory. Automatic: on for cards up to 8 GB.':
        '让 4-8 GB 显存的显卡不超出显存上限。自动：8 GB 及以下的显卡开启。',
    'Idle game workers sleep': '空闲工作线程休眠',
    'Frees CPU cores while the game\'s workers wait. Automatic: on for CPUs with up to 12 threads; '
    'on bigger CPUs it cost about 8%.':
        '在游戏的工作线程等待时释放 CPU 核心。自动：线程数不超过 12 的 CPU 开启；'
        '在核心更多的 CPU 上会损失约 8% 性能。',
    'PS4 thread priorities': 'PS4 线程优先级',
    'Game threads get the priorities they have on PS4. Automatic: off (the 4-core crash they were '
    'for is fixed by the job wait).':
        '让游戏线程获得 PS4 上的优先级。自动：关闭（它们原本要解决的四核崩溃已由作业等待修复）。',

    # ---- Trophies page ------------------------------------------------------------------------
    "The games' own trophy lists. A trophy shows here, and as a notice in the game, when you earn it.":
        '游戏自带的奖杯列表。获得奖杯后会显示在这里，并在游戏内弹出提示。',
    'All': '全部',
    'Earned': '已获得',
    'Locked': '未获得',
    'No trophy list for this game. Set the game folder on the Game page '
    '(it needs sce_sys/trophy/trophy0N.trp).':
        '此游戏没有奖杯列表。请在“游戏”页面设置游戏文件夹（需要 sce_sys/trophy/trophy0N.trp）。',
    'Hidden trophy': '隐藏奖杯',
    'Keep playing to find out how to earn it.': '继续游玩即可了解如何获得。',
    'Nothing here yet.': '这里还没有内容。',
    'Every trophy is earned.': '所有奖杯均已获得。',
    'Platinum': '白金',
    'Gold': '金',
    'Silver': '银',
    'Bronze': '铜',

    # ---- Cheats page --------------------------------------------------------------------------
    'Each cheat only affects its own game; changes apply when the game starts.':
        '每项作弊只影响对应的游戏；更改在游戏启动时生效。',
    'Infinite Health': '无限生命',
    'Infinite Ammo': '无限弹药',

    # ---- Advanced page ------------------------------------------------------------------------
    'Maintenance and options for testing.': '维护和测试选项。',
    'Launcher language': '启动器语言',
    'Interface language': '界面语言',
    'Automatic (Windows)': '自动（Windows）',
    'English': '英语',
    'This changes only the launcher. The game language is selected on the Game page.':
        '这只更改启动器。游戏语言在“游戏”页面选择。',
    'Write performance details to the log': '将性能详情写入日志',
    'Every 5 seconds the log gets the frame rate, the slowest frame and how busy the GPU side of '
    'the port was. Turn it on before you report low FPS and send the log with where it happened.':
        '每 5 秒在日志中记录帧率、最慢的帧以及移植版 GPU 侧的负载。反馈低帧率问题前请开启，'
        '并附上日志和出现问题的位置。',
    'Environment': '环境',
    'Extra variables for the game, NAME=value separated by spaces.':
        '游戏的额外变量，以空格分隔的 名称=值。',
    'Shader cache': '着色器缓存',
    'Compiled shaders are kept so the game does not stutter again. Clear the cache only when the '
    'picture is broken after an update.':
        '已编译的着色器会被保留，避免游戏再次卡顿。只有在更新后画面异常时才清除缓存。',
    'Open the saves folder': '打开存档文件夹',
    'Updates': '更新',
    'Look for a new version when the launcher starts': '启动器启动时查找新版本',
    'Releases page': '发布页面',
    'Shortcut name': '快捷方式名称',
    'Shortcut icon': '快捷方式图标',
    'Original icon': '原始图标',
    'Create shortcut': '创建快捷方式',
    'Add collection to Steam': '将合集添加到 Steam',
    'Use one image and adjust each Steam format separately.':
        '使用同一张图片，并分别为每种 Steam 格式调整裁剪。',
    'Portrait': '竖版封面',
    'Header': '横版横幅',
    'Hero': '主视觉大图',
    'Collection image': '合集图片',
    'The collection is in your Steam library. It starts with the settings saved in this launcher.':
        '合集已加入你的 Steam 库，会使用此启动器中保存的设置启动。',

    # ---- status line and messages -------------------------------------------------------------
    'Choose the game folder (the one with eboot.bin) on the Game page.':
        '请在“游戏”页面选择游戏文件夹（包含 eboot.bin 的那个）。',
    'Not in this folder: ': '不在此文件夹：',
    'No game folder yet.': '尚未设置游戏文件夹。',
    'Ready: {}': '就绪：{}',
    'Choose the game folder with eboot.bin.': '请选择包含 eboot.bin 的游戏文件夹。',
    'This game is not in the chosen folder.': '此游戏不在所选文件夹中。',
    'Could not save the input configuration: {}': '无法保存输入配置：{}',
    'see the Log page': '查看日志页面',
    'The game stopped: {}': '游戏已停止：{}',
    'Starting the next game of the collection…': '正在启动合集中的下一部游戏…',
    'Could not stop the game: {}': '无法停止游戏：{}',
    'Stopping the game…': '正在停止游戏…',
    'Could not clear the shader cache: {}': '无法清除着色器缓存：{}',
    'Shader cache cleared. The next start stutters for a while as it is rebuilt.':
        '着色器缓存已清除。下次启动时会因重建缓存而短暂卡顿。',
    'taskkill exited with code {}': 'taskkill 退出代码 {}',

    # ---- reserved keys ------------------------------------------------------------------------
    'Insert opens the in-game settings menu.': 'Insert 会打开游戏内设置菜单。',
    'Left Alt frees the mouse cursor while held.': '按住左 Alt 可释放鼠标光标。',

    # ---- choice boxes: game language ----------------------------------------------------------
    'English (United States)': '英语（美国）',
    'English (United Kingdom)': '英语（英国）',
    'French': '法语',
    'French (Canada)': '法语（加拿大）',
    'German': '德语',
    'Italian': '意大利语',
    'Spanish': '西班牙语',
    'Spanish (Latin America)': '西班牙语（拉丁美洲）',
    'Portuguese': '葡萄牙语',
    'Portuguese (Brazil)': '葡萄牙语（巴西）',
    'Dutch': '荷兰语',
    'Russian': '俄语',
    'Polish': '波兰语',
    'Turkish': '土耳其语',
    'Arabic': '阿拉伯语',
    'Japanese': '日语',
    'Korean': '韩语',
    'Chinese (Simplified)': '简体中文',
    'Chinese (Traditional)': '繁体中文',
    'Finnish': '芬兰语',
    'Swedish': '瑞典语',
    'Danish': '丹麦语',
    'Norwegian': '挪威语',

    # ---- choice boxes: display ----------------------------------------------------------------
    'Mailbox (low latency, no tearing)': 'Mailbox（低延迟，无撕裂）',
    'FIFO (VSync)': 'FIFO（垂直同步）',
    'FIFO Relaxed': 'FIFO Relaxed（宽松垂直同步）',
    'Immediate (tearing)': 'Immediate（有撕裂）',
    '30 FPS': '30 FPS',
    '60 FPS (as on PS4)': '60 FPS（与 PS4 相同）',
    '120 FPS': '120 FPS',
    '144 FPS (experimental)': '144 FPS（实验性）',
    '165 FPS (experimental)': '165 FPS（实验性）',
    '240 FPS (experimental)': '240 FPS（实验性）',
    '3840 × 2160 (4K)': '3840 × 2160（4K）',
    '2560 × 1080 (21:9)': '2560 × 1080（21:9）',
    '3440 × 1440 (21:9)': '3440 × 1440（21:9）',
    '3840 × 1600 (21:9)': '3840 × 1600（21:9）',
    '5120 × 1440 (32:9)': '5120 × 1440（32:9）',
    "1080p (the games' own)": '1080p（游戏原生）',
    '1440p': '1440p',
    '1620p': '1620p',
    '2160p (4K)': '2160p（4K）',
    "16:9 (the games' own)": '16:9（游戏原生）',
    '21:9 ultrawide': '21:9 超宽屏',
    '32:9 super ultrawide': '32:9 超级宽屏',
    'The shape of the window or screen': '跟随窗口或屏幕的形状',
    'Automatic (the Windows speaker setup)': '自动（跟随 Windows 扬声器设置）',
    'Stereo': '立体声',
    '5.1 surround': '5.1 环绕声',
    '7.1 surround': '7.1 环绕声',
    'FSR 1 (AMD FidelityFX, sharp)': 'FSR 1（AMD FidelityFX，锐利）',
    'Smooth (bilinear)': '平滑（双线性）',
    'Off': '关闭',
    'Low': '低',
    'Medium': '中',
    'High': '高',
    'Maximum': '最大',
    "Off (the game's own)": '关闭（使用游戏自带）',
    'TAA': 'TAA',
    'AMD FSR 3.1 (Native AA)': 'AMD FSR 3.1（原生抗锯齿）',
    'AMD FSR 4 (Native AA)': 'AMD FSR 4（原生抗锯齿）',
    'NVIDIA DLSS (DLAA, GeForce RTX)': 'NVIDIA DLSS（DLAA，GeForce RTX）',
    'AMD FSR 4.1.1 (Native AA)': 'AMD FSR 4.1.1（原生抗锯齿）',
    'Intel XeSS (Native AA, any GPU)': 'Intel XeSS（原生抗锯齿，任何显卡）',
    'AMD FSR 3 Frame Generation (any GPU)': 'AMD FSR 3 帧生成（任何显卡）',
    'NVIDIA DLSS Frame Generation (GeForce RTX 40/50)': 'NVIDIA DLSS 帧生成（GeForce RTX 40/50）',
    'On': '开启',
    'On + boost (NVIDIA: GPU clocks stay up)': '开启 + 加速（NVIDIA：GPU 保持高频）',
    'Automatic (follows the device you used last)': '自动（跟随最近使用的设备）',
    'Keyboard and mouse keys': '键盘和鼠标按键',
    'Xbox buttons': 'Xbox 按键',
    "PlayStation buttons (the game's own)": 'PlayStation 按键（游戏自带）',
    '2× (one generated frame)': '2×（生成一帧）',
    '3× (DLSS on GeForce RTX 50)': '3×（GeForce RTX 50 上的 DLSS）',
    '4× (DLSS on GeForce RTX 50)': '4×（GeForce RTX 50 上的 DLSS）',
    'Automatic': '自动',
    '1.0 (default)': '1.0（默认）',

    # ---- choice boxes: button actions and the controller names --------------------------------
    'Cross ✕': 'Cross ✕',
    'Circle ○': 'Circle ○',
    'Square □': 'Square □',
    'Triangle △': 'Triangle △',
    'L2 (aim)': 'L2（瞄准）',
    'R2 (fire)': 'R2（射击）',
    'Options': 'Options',
    'Touchpad': '触摸板',
    'D-pad up': '十字键上',
    'D-pad down': '十字键下',
    'D-pad left': '十字键左',
    'D-pad right': '十字键右',
    'Move forward': '前进',
    'Move back': '后退',
    'Move left': '左移',
    'Move right': '右移',
    'Look up': '视角上移',
    'Look down': '视角下移',
    'Look left': '视角左移',
    'Look right': '视角右移',
    'A / Cross': 'A / Cross',
    'B / Circle': 'B / Circle',
    'X / Square': 'X / Square',
    'Y / Triangle': 'Y / Triangle',
    'LB / L1': 'LB / L1',
    'RB / R1': 'RB / R1',
    'LT / L2': 'LT / L2',
    'RT / R2': 'RT / R2',
    'Left stick click / L3': '按下左摇杆 / L3',
    'Right stick click / R3': '按下右摇杆 / R3',
    'Start / Options': 'Start / Options',
    'Back / Share': 'Back / Share',
    'Touchpad click': '按下触摸板',
    'Share / Mic (misc)': 'Share / 麦克风（misc）',
    'Paddle 1': '背键 1',
    'Paddle 2': '背键 2',
    'Paddle 3': '背键 3',
    'Paddle 4': '背键 4',
    'Not assigned': '未绑定',
}
