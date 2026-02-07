<template>
	<div>
		<div id="particles"></div>
		<div class="register-container">
			<el-form v-if="pageFlag=='register'" ref="ruleForm" class="rgs-form animate__animated animate__backInDown" :model="ruleForm" :rules="rules">
				<div class="rgs-form2">
					<div class="title">基于招聘网站的大数据技术专业人才需求分析</div>
					<el-form-item class="list-item" v-if="tableName=='yonghu'">
						<div class="lable" :class="changeRules('zhanghao')?'required':''">账号：</div>
						<el-input  v-model="ruleForm.zhanghao"  autocomplete="off" placeholder="账号"  type="text"  />
					</el-form-item>
					<el-form-item class="list-item" v-if="tableName=='yonghu'">
						<div class="lable" :class="changeRules('xingming')?'required':''">姓名：</div>
						<el-input  v-model="ruleForm.xingming"  autocomplete="off" placeholder="姓名"  type="text"  />
					</el-form-item>
					<el-form-item class="list-item" v-if="tableName=='yonghu'">
						<div class="lable" :class="changeRules('mima')?'required':''">密码：</div>
						<el-input  v-model="ruleForm.mima"  autocomplete="off" placeholder="密码"  type="password"  />
					</el-form-item>
					<el-form-item class="list-item" v-if="tableName=='yonghu'">
						<div class="lable" :class="changeRules('mima')?'required':''">确认密码：</div>
						<el-input  v-model="ruleForm.mima2" autocomplete="off" placeholder="确认密码" type="password" />
					</el-form-item>
					<el-form-item class="list-item" v-if="tableName=='yonghu'">
						<div class="lable" :class="changeRules('xingbie')?'required':''">性别：</div>
						<el-select v-model="ruleForm.xingbie" placeholder="请选择性别" >
							<el-option
								v-for="(item,index) in yonghuxingbieOptions"
								v-bind:key="index"
								:label="item"
								:value="item">
							</el-option>
						</el-select>
					</el-form-item>
					<el-form-item class="list-item" v-if="tableName=='yonghu'">
						<div class="lable" :class="changeRules('lianxidianhua')?'required':''">联系电话：</div>
						<el-input  v-model="ruleForm.lianxidianhua"  autocomplete="off" placeholder="联系电话"  type="text"  />
					</el-form-item>
					<el-form-item class="list-item" v-if="tableName=='yonghu'">
						<div class="lable" :class="changeRules('touxiang')?'required':''">头像：</div>
						<file-upload
							tip="点击上传头像"
							action="file/upload"
							:limit="3"
							:multiple="true"
							:fileUrls="ruleForm.touxiang?ruleForm.touxiang:''"
							@change="yonghutouxiangUploadChange"
						></file-upload>
					</el-form-item>
					<div class="register-btn">
						<div class="register-btn1">
							<button type="button" class="r-btn" @click="login()">注册</button>
						</div>
						<div class="register-btn2">
							<div class="r-login" @click="close()">已有账号，点击登录</div>
						</div>
					</div>
				</div>
				<div class="idea-box1">注册</div>
				<div class="idea-box2">输入您的账号和密码以注册帐户</div>
			</el-form>
		</div>
	</div>
</template>

<script>
	import 'animate.css'
	require('@/utils/particles.js');
export default {
	data() {
		return {
			ruleForm: {
			},
			forgetForm: {},
            pageFlag : '',
			tableName:"",
			rules: {},
            yonghuxingbieOptions: [],
			particlesJson: {"retina_detect":true,"particles":{"number":{"density":{"value_area":800,"enable":true},"value":120},"move":{"straight":false,"random":false,"bounce":false,"enable":true,"attract":{"rotateX":600,"enable":false,"rotateY":1200},"speed":3,"direction":"none","out_mode":"out"},"color":{"value":"#fff"},"shape":{"image":{"width":100,"src":"img/github.svg","height":100},"polygon":{"nb_sides":5},"type":"circle","stroke":{"color":"#000000","width":0}},"size":{"anim":{"size_min":0.1,"sync":false,"enable":false,"speed":20},"random":true,"value":1},"line_linked":{"width":1,"distance":40,"color":"#ffffff","opacity":1,"enable":true},"opacity":{"anim":{"opacity_min":0.1,"sync":false,"enable":false,"speed":1},"random":false,"value":0.5}},"interactivity":{"detect_on":"canvas","events":{"resize":true,"onclick":{"mode":"repulse","enable":true},"onhover":{"mode":"bubble","enable":true}},"modes":{"grab":{"distance":400,"line_linked":{"opacity":1}},"bubble":{"duration":2,"distance":250,"size":0,"opacity":0,"speed":3},"repulse":{"duration":0.4,"distance":400},"push":{"particles_nb":4},"remove":{"particles_nb":2}}}}
		};
	},
	mounted(){
		particlesJS('particles',this.particlesJson);
		this.pageFlag = this.$route.query.pageFlag
		if(this.$route.query.pageFlag=='register'){
			
			let table = this.$storage.get("loginTable");
			this.tableName = table;
			if(this.tableName=='yonghu'){
				this.ruleForm = {
					zhanghao: '',
					xingming: '',
					mima: '',
					xingbie: '',
					lianxidianhua: '',
					touxiang: '',
				}
			}
			if ('yonghu' == this.tableName) {
				this.rules.zhanghao = [{ required: true, message: '请输入账号', trigger: 'blur' }]
			}
			if ('yonghu' == this.tableName) {
				this.rules.xingming = [{ required: true, message: '请输入姓名', trigger: 'blur' }]
			}
			if ('yonghu' == this.tableName) {
				this.rules.mima = [{ required: true, message: '请输入密码', trigger: 'blur' }]
			}
			this.yonghuxingbieOptions = "男,女".split(',')
		}
	},
	created() {
	},
	destroyed() {
		  	},
	methods: {
		changeRules(name){
			if(this.rules[name]){
				return true
			}
			return false
		},
		// 获取uuid
		getUUID () {
			return new Date().getTime();
		},
		close(){
			this.$router.push({ path: "/login" });
		},
        yonghutouxiangUploadChange(fileUrls) {
            this.ruleForm.touxiang = fileUrls;
        },

        // 多级联动参数


		// 注册
		login() {
			var url=this.tableName+"/register";
			if((!this.ruleForm.zhanghao) && `yonghu` == this.tableName){
				this.$message.error(`账号不能为空`);
				return
			}
			if((!this.ruleForm.xingming) && `yonghu` == this.tableName){
				this.$message.error(`姓名不能为空`);
				return
			}
			if((!this.ruleForm.mima) && `yonghu` == this.tableName){
				this.$message.error(`密码不能为空`);
				return
			}
			if((this.ruleForm.mima!=this.ruleForm.mima2) && `yonghu` == this.tableName){
				this.$message.error(`两次密码输入不一致`);
				return
			}
			if(`yonghu` == this.tableName && this.ruleForm.lianxidianhua &&(!this.$validate.isMobile(this.ruleForm.lianxidianhua))){
				this.$message.error(`联系电话应输入手机格式`);
				return
			}
            if(this.ruleForm.touxiang!=null) {
                this.ruleForm.touxiang = this.ruleForm.touxiang.replace(new RegExp(this.$base.url,"g"),"");
            }
			this.$http({
				url: url,
				method: "post",
				data:this.ruleForm
			}).then(({ data }) => {
				if (data && data.code === 0) {
					this.$message({
						message: "注册成功",
						type: "success",
						duration: 1500,
						onClose: () => {
							this.$router.replace({ path: "/login" });
						}
					});
				} else {
					this.$message.error(data.msg);
				}
			});
		}
	}
};
</script>

<style lang="scss" scoped>
.register-container {
	position: relative;
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
	.rgs-form {
		.rgs-form2 {
		margin: 10px 0 ;
		width: 500px;
		}
		border-radius: 0;
		padding: 20px 40px 40px 157px;
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
		.title {
			padding: 0 40px;
			margin: 0 0 20px 0;
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
			border-radius: 8px;
			padding: 0;
			margin: 0 0 20px;
			background: none;
			display: flex;
			width: calc(100% - 0px);
			align-items: center;
			position: relative;
			flex-wrap: wrap;
			/deep/ .el-form-item__content {
				display: block;
				width: 100%;
			}
			.lable {
				padding: 0 5px 0 0;
				color: #000;
				left: 10px;
				width: 130px;
				font-size: 16px;
				line-height: 50px ;
				position: absolute !important;
				text-align: left;
			}
			.el-input {
				width: 100%;
			}
			.el-input /deep/ .el-input__inner {
				border: 1px solid #333333;
				border-radius: 0px;
				padding: 0 120px;
				color: #666;
				background: none;
				width: 100%;
				font-size: 16px;
				height: 50px ;
			}
			.el-input /deep/ .el-input__inner:focus {
				border: 1px solid #333333;
				border-radius: 0px;
				padding: 0 120px;
				color: #666;
				background: none;
				width: 100%;
				font-size: 16px;
				height: 50px ;
			}
			.el-input-number {
				width: 100%;
			}
			.el-input-number /deep/ .el-input__inner {
				text-align: center;
				border: 1px solid #333333;
				border-radius: 0px;
				padding: 0 120px;
				color: #666;
				background: none;
				width: 100%;
				font-size: 16px;
				height: 50px ;
			}
			.el-input-number /deep/ .el-input__inner:focus {
				border: 1px solid #333333;
				border-radius: 0px;
				padding: 0 120px;
				color: #666;
				background: none;
				width: 100%;
				font-size: 16px;
				height: 50px ;
			}
			.el-input-number /deep/ .el-input-number__decrease {
				display: none;
			}
			.el-input-number /deep/ .el-input-number__increase {
				display: none;
			}
			.el-select {
				width: 100%;
			}
			.el-select /deep/ .el-input__inner {
				border: 1px solid #333333;
				border-radius: 0px;
				padding: 0 120px;
				color: #666;
				background: none;
				width: 100%;
				font-size: 16px;
				height: 50px ;
			}
			.el-select /deep/ .el-input__inner:focus {
				border: 1px solid #333333;
				border-radius: 0px;
				padding: 0 120px;
				color: #666;
				background: none;
				width: 100%;
				font-size: 16px;
				height: 50px ;
			}
			.el-date-editor {
				width: 100%;
			}
			.el-date-editor /deep/ .el-input__inner {
				border: 1px solid #333333;
				border-radius: 0px;
				padding: 0 120px;
				color: #666;
				background: none;
				width: 100%;
				font-size: 16px;
				height: 50px ;
			}
			.el-date-editor /deep/ .el-input__inner:focus {
				border: 1px solid #333333;
				border-radius: 0px;
				padding: 0 120px;
				color: #666;
				background: none;
				width: 100%;
				font-size: 16px;
				height: 50px ;
			}
			.el-date-editor.el-input {
				width: 100%;
			}
			/deep/ .el-upload--picture-card {
				background: transparent;
				border: 0;
				border-radius: 0;
				width: auto;
				height: auto;
				line-height: initial;
				vertical-align: middle;
			}
			/deep/ .upload .upload-img {
				border: 1px solid #333333;
				padding: 0 0px;
				margin: 0 0 0 80px;
				color: #666;
				background: none;
				width: 100px;
				font-size: 16px;
				line-height: 50px;
				height: 50px;
			}
			/deep/ .el-upload-list .el-upload-list__item {
				border: 1px solid #333333;
				padding: 0 0px;
				margin: 0 0 0 80px;
				color: #666;
				background: none;
				width: 100px;
				font-size: 16px;
				line-height: 50px;
				height: 50px;
			}
			/deep/ .el-upload .el-icon-plus {
				border: 1px solid #333333;
				padding: 0 0px;
				margin: 0 0 0 80px;
				color: #666;
				background: none;
				width: 100px;
				font-size: 16px;
				line-height: 50px;
				height: 50px;
			}
			/deep/ .el-upload__tip {
				margin: 0 0 0 80px;
				color: #666;
				font-size: 15px;
			}
			/deep/ .el-input__inner::placeholder {
				color: #999;
				font-size: 16px;
			}
			.required {
				position: relative;
			}
			.required::after{
				color: red;
				left: -10px;
				line-height: 50px ;
				position: inherit;
				content: "*";
				order: -1;
			}
			.editor {
				border: 1px solid #333333;
				background: none;
				width: 500px;
				height: auto;
			}
			.editor>.avatar-uploader {
				line-height: 0;
				height: 0;
			}
		}
		.list-item.email {
			input {
				border: 1px solid #333333;
				border-radius: 0px;
				padding: 0 120px;
				color: #666;
				background: none;
				width: 100%;
				font-size: 16px;
				height: 50px ;
			}
			input:focus {
				border: 1px solid #333333;
				border-radius: 0px;
				padding: 0 120px;
				color: #666;
				background: none;
				width: 100%;
				font-size: 16px;
				height: 50px ;
			}
			input::placeholder {
				color: #999;
				font-size: 16px;
			}
			button {
				border: 0px solid #e6e6e6;
				cursor: pointer;
				border-radius: 5px;
				padding: 0;
				margin: 0 0 0 10px;
				color: #fff;
				background: #02a79c;
				width: 120px;
				font-size: 15px;
				height: 50px ;
			}
			button:hover {
				opacity: 0.8;
			}
		}
		.register-btn {
			margin: 60px 0 0 0px;
			display: flex;
			width: 100%;
			flex-wrap: wrap;
		}
		.register-btn1 {
			width: 30%;
			order: 1;
		}
		.register-btn2 {
			flex: 1;
			line-height: 60px;
			order: 2;
			height: 60px;
		}
		.r-btn {
			border: 0px solid rgba(0, 0, 0, 1);
			cursor: pointer;
			border-radius: 5px;
			padding: 0 10px;
			margin: 0 0 10px;
			color: #fff;
			background: #02A79C;
			font-weight: 700;
			width: 136px;
			font-size: 24px;
			min-width: 68px;
			height: 60px;
		}
		.r-btn:hover {
			border: 0px solid rgba(0, 0, 0, 1);
			opacity: 0.8;
		}
		.r-login {
			cursor: pointer;
			padding: 0;
			color: #02A79C;
			display: inline-block;
			width: 100%;
			font-size: 15px;
			line-height: 40px;
			text-align: right;
		}
		.r-login:hover {
			opacity: 1;
		}
	}
	.idea-box1 {
		background: none;
		font-weight: 600;
		display: none;
		width: 560px;
		font-size: 20px;
		height: 30px;
		order: -2;
	}
	.idea-box2 {
		margin: 5px 0 40px;
		background: #fff;
		display: none;
		width: 100%;
		font-size: 16px;
		height: 30px;
		order: -1;
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
	::-webkit-scrollbar {
	  display: none;
	}
</style>
