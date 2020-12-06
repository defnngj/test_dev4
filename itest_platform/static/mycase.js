
var getCaseInfo = function(){
    console.log(" 这个函数调用后端一个case的信息过来！");
    var url = window.location.href;
    var caseId = url.split("/")[5];
    console.log(caseId)
    
    // 调用获取select数据列表
    $.get("/api/get_case_info/"+caseId+"/", {}, 
    function (resp) {
        if (resp.code == 200) {
            console.log(resp.data.name);
            // 请求的URL
            $("#req_url").val(resp.data.url);
            // 用例的名称
            $("#case_name").val(resp.data.name);
            // 响应的结果
            $("#result").val(resp.data.response);
            // 响应断言
            $("#assert").val(resp.data.response_assert);

            //请求方法
            if(resp.data.method == 1){
                $("#method").val("GET");
            }else if (resp.data.method == 2){
                $("#method").val("POST");
            }else {
                window.alert("不支持请求方法")
            }

            //请求类型
            if(resp.data.request_type == 1){
                $('#data').prop('checked',true);
            }else if (resp.data.request_type == 2){
                $("#json").prop('checked',true);
            }else {
                window.alert("不支持参数类型")
            }

            // 参数的值
            // 参数
            var par_json = JSON.parse(resp.data.request_body);
            parameterEditor.set(par_json);

            // 项目/模块
            console.log("调用初始化列表")
            SelectInit(resp.data.project, resp.data.module)

        }else{
            window.alert(resp.msg);
        }

    });

}