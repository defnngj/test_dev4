
var hello = function(name){
    console.log("hello myselect.js: " + name);
}

//初始化 “项目>模块” 二级联动菜单
var SelectInit = function (defaultProjectId, defaultModuleId) {

    var cmbProject = document.getElementById("selectProject");
    var cmbModule = document.getElementById("selectModule");

    var dataList = [];

    //设置默认选项
    function setDefaultOption(obj, id) {
        for (let i = 0; i < obj.options.length; i++) {
            if (obj.options[i].value == id) {
                obj.selectedIndex = i;
                return;
            }
        }
    }

    //创建下拉选项
    function addOption(cmb, obj) {
        var option = document.createElement("option");
        cmb.options.add(option);
        option.innerHTML = obj.name;
        option.value = obj.id;
    }

    //改变项目
    function changeProject() {
        cmbModule.options.length = 0;
        var pid = cmbProject.options[cmbProject.selectedIndex].value; 

        for (let i = 0; i < dataList.length; i++) {
            if(dataList[i].id == pid) {
                var modules = dataList[i].moduleList;
                for(var j=0; j< modules.length; j++){
                    addOption(cmbModule, modules[j]);
                }
            }

        }

        setDefaultOption(cmbModule, defaultModuleId);
    }

    function getSelectData() {
        // 调用获取select数据列表
        $.get("/api/select_data/", {

        }, 
        function (resp) {
            if (resp.code == 10200) {
                dataList = resp.data;
                //遍历项目
                for (let i = 0; i < dataList.length; i++) {
                    addOption(cmbProject, dataList[i]);
                }

                setDefaultOption(cmbProject, defaultProjectId);
                changeProject();
                cmbProject.onchange = changeProject;
            }

            setDefaultOption(cmbProject, defaultProjectId);

        });
    }

    // 调用getSelectData函数
    getSelectData();

};
