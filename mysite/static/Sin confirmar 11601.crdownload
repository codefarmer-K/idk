// tabs.js
function openTab(event, tabId) {
    // 隐藏所有选项卡内容
    const tabPanels = document.querySelectorAll('.tab-panel');
    tabPanels.forEach(panel => panel.classList.remove('active'));

    // 移除所有按钮的激活状态
    const tabButtons = document.querySelectorAll('.tab-button');
    tabButtons.forEach(button => button.classList.remove('active'));

    // 显示选中的选项卡内容，并将该按钮设置为激活状态
    document.getElementById(tabId).classList.add('active');
    event.currentTarget.classList.add('active');
}
