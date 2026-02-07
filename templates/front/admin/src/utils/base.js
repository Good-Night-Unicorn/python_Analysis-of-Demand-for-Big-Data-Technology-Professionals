const base = {
    get() {
        return {
            url : "http://localhost:8080/djangosk189641/",
            name: "djangosk189641",
            // 退出到首页链接
            indexUrl: 'http://localhost:8080/front/dist/index.html'
        };
    },
    getProjectName(){
        return {
            projectName: "基于招聘网站的大数据技术专业人才需求分析"
        } 
    }
}
export default base
