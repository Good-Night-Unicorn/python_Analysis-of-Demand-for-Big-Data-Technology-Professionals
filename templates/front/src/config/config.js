export default {
	baseUrl: 'http://localhost:8080/djangosk189641/',
	name: '/djangosk189641',
	indexNav: [
		{
			name: '全国职位',
			url: '/index/zhipindsj',
		},
		{
			name: '公告栏',
			url: '/index/news'
		},
	],
	cateList: [
		{
			name: '公告栏',
			refTable: 'newstype',
			refColumn: 'typename',
		},
	]
}
