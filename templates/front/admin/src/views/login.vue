<template>
	<div>
		<div id="particles"></div>
		<div class="login-container">
			<el-form class="login_form animate__animated animate__slideInDown">
				<div class="login_form2">
					<div class="title-container">基于招聘网站的大数据技术专业人才需求分析</div>
					<div v-if="loginType==1" class="list-item">
						<div class="lable">
							账号：
						</div>
						<input placeholder="请输入账号：" name="username" type="text" v-model="rulesForm.username">
					</div>
					<div v-if="loginType==1" class="list-item">
						<div class="lable">
							密码：
						</div>
						<div class="password-box">
							<input placeholder="请输入密码：" name="password" :type="showPassword?'text':'password'" v-model="rulesForm.password">
							<span class="icon iconfont" :class="showPassword?'icon-liulan13':'icon-liulan17'" @click="showPassword=!showPassword"></span>
						</div>
					</div>

					<div class="list-item " v-if="roles.length>1">
						<div class="lable">
							角色：
						</div>
						<div prop="loginInRole" class="list-type">
							<el-radio v-if="loginType==1||(loginType==2&&item.roleName!='管理员')" v-for="item in roles" v-bind:key="item.roleName" v-model="rulesForm.role" :label="item.roleName">{{item.roleName}}</el-radio>
						</div>
					</div>

		
					<div class="login-btn">
						<div class="login-btn1">
							<el-button v-if="loginType==1" type="primary" @click="login()" class="loginInBt">登录</el-button>
						</div>
						<div class="login-btn2">
						</div>
						<div class="login-btn3">
						</div>
					</div>
				</div>
			</el-form>
		</div>
	</div>
</template>
<script>
	import 'animate.css'
	import menu from "@/utils/menu";
	require('@/utils/particles.js')
	export default {
		data() {
			return {
				verifyCheck2: false,
				flag: false,
				baseUrl:this.$base.url,
				loginType: 1,
				rulesForm: {
					username: "",
					password: "",
					role: "",
				},
				menus: [],
				roles: [],
				tableName: "",
				showPassword: false,
				particlesJson: {"retina_detect":true,"particles":{"number":{"density":{"value_area":800,"enable":true},"value":120},"move":{"straight":false,"random":false,"bounce":false,"enable":true,"attract":{"rotateX":600,"enable":false,"rotateY":1200},"speed":3,"direction":"none","out_mode":"out"},"color":{"value":"#fff"},"shape":{"image":{"width":100,"src":"img/github.svg","height":100},"polygon":{"nb_sides":5},"type":"circle","stroke":{"color":"#000000","width":0}},"size":{"anim":{"size_min":0.1,"sync":false,"enable":false,"speed":20},"random":true,"value":1},"line_linked":{"width":1,"distance":40,"color":"#ffffff","opacity":1,"enable":true},"opacity":{"anim":{"opacity_min":0.1,"sync":false,"enable":false,"speed":1},"random":false,"value":0.5}},"interactivity":{"detect_on":"canvas","events":{"resize":true,"onclick":{"mode":"repulse","enable":true},"onhover":{"mode":"bubble","enable":true}},"modes":{"grab":{"distance":400,"line_linked":{"opacity":1}},"bubble":{"duration":2,"distance":250,"size":0,"opacity":0,"speed":3},"repulse":{"duration":0.4,"distance":400},"push":{"particles_nb":4},"remove":{"particles_nb":2}}}}
			};
		},
		mounted() {
			let menus = menu.list();
			this.menus = menus;

			for (let i = 0; i < this.menus.length; i++) {
				if (this.menus[i].hasBackLogin=='是') {
					this.roles.push(this.menus[i])
				}
			}

			particlesJS('particles',this.particlesJson);
		},
		created() {

		},
		destroyed() {
		},
		components: {
		},
		methods: {

			//注册
			register(tableName){
				this.$storage.set("loginTable", tableName);
				this.$router.push({path:'/register',query:{pageFlag:'register'}})
			},
			// 登陆
			login() {

				if (!this.rulesForm.username) {
					this.$message.error("请输入用户名");
					return;
				}
				if (!this.rulesForm.password) {
					this.$message.error("请输入密码");
					return;
				}
				if(this.roles.length>1) {
					if (!this.rulesForm.role) {
						this.$message.error("请选择角色");
						return;
					}

					let menus = this.menus;
					for (let i = 0; i < menus.length; i++) {
						if (menus[i].roleName == this.rulesForm.role) {
							this.tableName = menus[i].tableName;
						}
					}
				} else {
					this.tableName = this.roles[0].tableName;
					this.rulesForm.role = this.roles[0].roleName;
				}
		
				this.loginPost()
			},
			loginPost() {
				this.$http({
					url: `${this.tableName}/login?username=${this.rulesForm.username}&password=${this.rulesForm.password}`,
					method: "post"
				}).then(({ data }) => {
					if (data && data.code === 0) {
						this.$storage.set("Token", data.token);
						this.$storage.set("role", this.rulesForm.role);
						this.$storage.set("sessionTable", this.tableName);
						this.$storage.set("adminName", this.rulesForm.username);
						this.$nextTick(()=>{
							this.$http({
								url: this.tableName + '/session',
								method: "get"
							}).then(({
								data
							}) => {
								if (data && data.code === 0) {
									if(this.tableName == 'yonghu') {
										this.$storage.set('headportrait',data.data.touxiang)
									}
									if(this.tableName == 'users') {
										this.$storage.set('headportrait',data.data.image)
									}
									this.$storage.set('userForm',JSON.stringify(data.data))
									this.$storage.set('userid',data.data.id);
								} else {
									let message = this.$message
									message.error(data.msg);
								}
								if(this.boardAuth('hasBoard','查看',this.rulesForm.role)) {
									this.$router.replace({ path: "/board" });
								}else {
									this.$router.replace({ path: "/" });
								}
							});
						})
					} else {
						this.$message.error(data.msg);
					}
				});
			},
		}
	}
</script>

<style lang="scss" scoped>
.login-container {
	min-height: 100vh;
	position: relative;
	background-repeat: no-repeat;
	background-position: center center;
	background-size: cover;
	background: url(http://codegen.caihongy.cn/20250302/96674c96fe3440f4be32380636b46f5f.jpg);
	background-repeat: no-repeat;
	overflow: hidden;
	background-size: cover !important;
	background: url(http://codegen.caihongy.cn/20250302/96674c96fe3440f4be32380636b46f5f.jpg);
	display: flex;
	width: 100%;
	min-height: 100vh;
	justify-content: flex-end;
	align-items: center;
	background-position: center center;
	position: relative;

	.login_form {
		border-radius: 0;
		padding: 267px 40px 40px 157px;
		margin: 0;
		z-index: 1000;
		flex-direction: column;
		background: linear-gradient( 180deg, #F0F4F9 0%, #DFFAFF 100%);
		display: flex;
		width: 50%;
		min-height: 100vh;
		align-items: flex-start;
		flex-wrap: wrap;
		height: auto;
		.login_form2 {
			margin: 10px 0 ;
			width: 500px;
		}
		.title-container {
			padding: 0 40px;
			margin: 0 0 10px 0;
			z-index: 2;
			color: #02A79C;
			background: none;
			font-weight: 500;
			width: 100%;
			font-size: 20px;
			line-height: 40px;
			text-align: left;
		}
		.list-item {
			padding: 0;
			margin: 15px 0 20px 10px;
			background: none;
			display: flex;
			width: 500px;
			align-items: center;
			position: relative;
			height: 50px;
			.lable {
				border: 0 ;
				z-index: 2;
				color: #333333;
				left: 10px;
				letter-spacing: 1px;
				width: auto;
				font-size: 16px;
				line-height: 50px;
				position: absolute;
				text-align: left;
				min-width: 60px;
				height: 50px;
			}
			input {
				border: 1px solid #333333;
				padding: 0 72px;
				color: #666;
				flex: 1;
				background: none;
				width: 100%;
				font-size: 16px;
				position: absolute;
				height: 50px;
			}
			input:focus {
				border: 1px solid #333333;
				padding: 0 72px;
				outline: none;
				color: #666;
				flex: 1;
				background: #fff;
				width: 100%;
				font-size: 16px;
				position: absolute;
				height: 50px;
			}
			.password-box {
				display: flex;
				width: 100%;
				align-items: center;
				input {
					border: 1px solid #333333;
					padding: 0 72px;
					outline: none;
					color: #666;
					flex: 1;
					background: none;
					width: 100%;
					font-size: 16px;
					line-height: 50px;
					height: 50px;
				}
				input:focus {
					border: 1px solid #333333;
					padding: 0 72px;
					outline: none;
					color: #666;
					flex: 1;
					width: 100%;
					font-size: 16px;
					line-height: 50px;
					height: 50px;
				}
				.iconfont {
					cursor: pointer;
					z-index: 1;
					color: #000;
					top: 0;
					font-size: 16px;
					line-height: 44px;
					position: absolute;
					right: 5px;
				}
			}
			input::placeholder {
				color: #999;
				font-size: 16px;
			}
		}
		.list-type {
			border: 1px solid #333333;
			padding: 0 72px;
			color: #666;
			display: flex;
			font-size: 16px;
			min-height: 50px;
			line-height: 50px;
			flex-wrap: wrap;
			outline: none;
			flex: 1;
			width: 100%;
			align-items: center;
			height: auto;
			/deep/ .el-radio__input .el-radio__inner {
				background: rgba(53, 53, 53, 0);
				border-color: #666;
			}
			/deep/ .el-radio__input.is-checked .el-radio__inner {
				background: #02A79C;
				border-color: #02A79C;
			}
			/deep/ .el-radio__label {
				color: #666;
				font-size: 16px;
			}
			/deep/ .el-radio__input.is-checked+.el-radio__label {
				color: #02A79C;
				font-size: 16px;
			}
		}
		.login-btn {
			margin: 30px 0 0 10px;
			display: flex;
			width: 100%;
			justify-content: center;
			flex-wrap: wrap;
			.login-btn1 {
				width: auto;
				order: 1;
			}
			.login-btn2 {
				padding: 0;
				margin: 00;
				display: flex;
				width: auto;
				flex-wrap: wrap;
				order: 3;
			}
			.login-btn3 {
				width: 100%;
				line-height: 60px;
				order: 20;
				height: 60px;
			}
			.loginInBt {
				border: 0px solid rgba(0, 0, 0, 1);
				cursor: pointer;
				border-radius: 5px;
				padding: 0 10px;
				margin: 0 10px 10px;
				color: #fff;
				background: #02A79C;
				font-weight: 700;
				width: 130px;
				font-size: 24px;
				min-width: 68px;
				height: 50px;
			}
			.loginInBt:hover {
				opacity: 0.8;
			}
			.register {
				border: 2px solid #B8B8B8;
				cursor: pointer;
				border-radius: 10px;
				padding: 0 10px;
				margin: 0 10px 10px 0;
				color: #B8B8B8;
				background: none;
				width: auto;
				font-size: 16px;
				min-width: 130px;
				height: 50px;
			}
			.register:hover {
				opacity: 0.8;
			}
			.forget {
				border: 0;
				cursor: pointer;
				border-radius: 0;
				padding: 0;
				margin: 0 10px 10px 0;
				color: #02A79C;
				background: none;
				width: 100%;
				font-size: 15px;
				text-align: right;
				height: 34px;
			}
			.forget:hover {
				color: #0d6efd;
				opacity: 1;
			}
		}
	}
}

	#particles{
		background-repeat: no-repeat;
		z-index: 1;
		background-size: cover;
		width: 100%;
		position: absolute;
		background-position: 50% 50%;
		height: 100%;
	}
</style>
