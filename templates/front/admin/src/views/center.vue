<template>
	<div :style='{"padding":"50px 20px 20px","background":"none","fontSize":"15px"}'>
		<el-form
			:style='{"border":"1px solid #BFBFBF","padding":"42px  25% 42px  15%","margin":"0 auto","flexWrap":"wrap","background":"#fff","display":"flex"}'
			class="add-update-preview"
			ref="ruleForm"
			:model="ruleForm"
			label-width="180px"
		>
				<el-form-item :style='{"border":"0px solid #eee","width":"100%","padding":"0","margin":"0 0 20px!important"}'   v-if="flag=='yonghu'"  label="账号" prop="zhanghao">
					<el-input v-model="ruleForm.zhanghao" readonly placeholder="账号" clearable></el-input>
				</el-form-item>
				<el-form-item :style='{"border":"0px solid #eee","width":"100%","padding":"0","margin":"0 0 20px!important"}'   v-if="flag=='yonghu'"  label="姓名" prop="xingming">
					<el-input v-model="ruleForm.xingming"  placeholder="姓名" clearable></el-input>
				</el-form-item>
				<el-form-item :style='{"border":"0px solid #eee","width":"100%","padding":"0","margin":"0 0 20px!important"}' v-if="flag=='yonghu'"  label="性别" prop="xingbie">
					<el-select v-model="ruleForm.xingbie"  placeholder="请选择性别">
						<el-option
							v-for="(item,index) in yonghuxingbieOptions"
							v-bind:key="index"
							:label="item"
							:value="item">
						</el-option>
					</el-select>
				</el-form-item>
				<el-form-item :style='{"border":"0px solid #eee","width":"100%","padding":"0","margin":"0 0 20px!important"}'   v-if="flag=='yonghu'"  label="联系电话" prop="lianxidianhua">
					<el-input v-model="ruleForm.lianxidianhua"  placeholder="联系电话" clearable></el-input>
				</el-form-item>
				<el-form-item :style='{"border":"0px solid #eee","width":"100%","padding":"0","margin":"0 0 20px!important"}' v-if="flag=='yonghu'" label="头像" prop="touxiang">
					<file-upload
						tip="点击上传头像"
						action="file/upload"
						:limit="3"
						:multiple="true"
						:fileUrls="ruleForm.touxiang?ruleForm.touxiang:''"
						@change="yonghutouxiangUploadChange"
					></file-upload>
				</el-form-item>
				<el-form-item :style='{"border":"0px solid #eee","width":"100%","padding":"0","margin":"0 0 20px!important"}' v-if="flag=='users'" label="用户名" prop="username">
					<el-input v-model="ruleForm.username" placeholder="用户名"></el-input>
				</el-form-item>
				<el-form-item :style='{"border":"0px solid #eee","width":"100%","padding":"0","margin":"0 0 20px!important"}' v-if="flag=='users'" label="头像" prop="image">
					<file-upload
						tip="点击上传头像"
						action="file/upload"
						:limit="1"
						:multiple="false"
						:fileUrls="ruleForm.image?ruleForm.image:''"
						@change="usersimageUploadChange"
					></file-upload>
				</el-form-item>
				<el-form-item :style='{"width":"100%","padding":"0","margin":"30px 0"}'>
					<el-button class="btn3" :style='{"border":"2px solid #02A79C","cursor":"pointer","padding":"0 10px","margin":"0 10px 0 0","color":"#02A79C","borderRadius":"4px","background":"none","width":"auto","fontSize":"16px","minWidth":"110px","height":"40px"}' type="primary" @click="onUpdateHandler">
						<span class="icon iconfont icon-xihuan" :style='{"margin":"0 2px","fontSize":"14px","color":"#fff","display":"none","height":"40px"}'></span>
						提交
					</el-button>
				</el-form-item>
		</el-form>
	</div>
</template>
<script>
// 校验引入
import { 
	isMobile,
} from "@/utils/validate";

export default {
	data() {
		return {
			ruleForm: {},
			flag: '',
			usersFlag: false,
			yonghuxingbieOptions: [],
			};
		},
		mounted() {
			var table = this.$storage.get("sessionTable");
			this.flag = table;
			this.$http({
				url: `${this.$storage.get("sessionTable")}/session`,
				method: "get"
			}).then(({ data }) => {
				if (data && data.code === 0) {

					this.ruleForm = data.data;
				} else {
					this.$message.error(data.msg);
				}
			});
			this.yonghuxingbieOptions = "男,女".split(',')
		},
		methods: {
		yonghutouxiangUploadChange(fileUrls) {
			this.ruleForm.touxiang = fileUrls;
		},
		usersimageUploadChange(fileUrls) {
			this.ruleForm.image = fileUrls;
		},
		onUpdateHandler() {
			if((!this.ruleForm.zhanghao)&& 'yonghu'==this.flag){
				this.$message.error('账号不能为空');
				return
			}


			if((!this.ruleForm.xingming)&& 'yonghu'==this.flag){
				this.$message.error('姓名不能为空');
				return
			}


			if((!this.ruleForm.mima)&& 'yonghu'==this.flag){
				this.$message.error('密码不能为空');
				return
			}





			if( 'yonghu' ==this.flag && this.ruleForm.lianxidianhua&&(!isMobile(this.ruleForm.lianxidianhua))){
				this.$message.error(`联系电话应输入手机格式`);
				return
			}


			if(this.ruleForm.touxiang!=null) {
				this.ruleForm.touxiang = this.ruleForm.touxiang.replace(new RegExp(this.$base.url,"g"),"");
			}
			if('users'==this.flag && this.ruleForm.username.trim().length<1) {
				this.$message.error(`用户名不能为空`);
				return	
			}
			if(this.flag=='users'){
				this.ruleForm.image = this.ruleForm.image.replace(new RegExp(this.$base.url,"g"),"")
			}
			this.$http({
				url: `${this.$storage.get("sessionTable")}/update`,
				method: "post",
				data: this.ruleForm
			}).then(({ data }) => {
				if (data && data.code === 0) {
					if(this.flag=='users'){
						this.$storage.set('headportrait',this.ruleForm.image)
					}
					this.$message({
						message: "修改信息成功",
						type: "success",
						duration: 1500,
						onClose: () => {
							window.location.reload();
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
	.el-date-editor.el-input {
		width: auto;
	}
	
	.add-update-preview .el-form-item /deep/ .el-form-item__label {
				border: 0px solid #B1DBE0;
				padding: 0 10px 0 0;
				margin: 0;
				color: #02A79C;
				background: none;
				font-weight: 400;
				width: 180px;
				font-size: 16px;
				line-height: 40px;
				text-align: right;
				height: auto;
			}
	
	.add-update-preview .el-form-item /deep/ .el-form-item__content {
		margin-left: 180px;
	}
	
	.add-update-preview .el-input /deep/ .el-input__inner {
				border-radius: 0px;
				padding: 0 12px;
				margin: 0;
				color: #85B3B9;
				width: auto;
				font-size: 14px;
				border-color: #B1DBE0;
				border-width: 1px;
				border-style: solid ;
				min-width: 100%;
				height: 40px;
			}
	
	.add-update-preview .el-select /deep/ .el-input__inner {
				border-radius: 0px;
				padding: 0 12px;
				margin: 0;
				color: #85B3B9;
				width: auto;
				font-size: 14px;
				border-color: #B1DBE0;
				border-width: 1px;
				border-style: solid ;
				min-width: 100%;
				height: 40px;
			}
	
	.add-update-preview .el-date-editor /deep/ .el-input__inner {
				border-radius: 0px;
				padding: 0 30px;
				color: #85B3B9;
				width: auto;
				font-size: 14px;
				border-color: #B1DBE0;
				border-width: 1px;
				border-style: solid ;
				min-width: 100%;
				height: 40px;
			}
	
	.add-update-preview /deep/ .el-upload--picture-card {
		background: transparent;
		border: 0;
		border-radius: 0;
		width: auto;
		height: auto;
		line-height: initial;
		vertical-align: middle;
	}
	
	.add-update-preview /deep/ .el-upload-list .el-upload-list__item {
				border-radius: 0px;
				padding: 0 12px;
				color: #85B3B9;
				font-weight: 500;
				object-fit: cover;
				width: 100px;
				font-size: 32px;
				border-color: #B1DBE0;
				border-width: 1px;
				line-height: 70px;
				border-style: solid ;
				height: 70px;
			}
	
	.add-update-preview /deep/ .el-upload .el-icon-plus {
				border-radius: 0px;
				padding: 0 12px;
				color: #85B3B9;
				font-weight: 500;
				object-fit: cover;
				width: 100px;
				font-size: 32px;
				border-color: #B1DBE0;
				border-width: 1px;
				line-height: 70px;
				border-style: solid ;
				height: 70px;
			}
	
	.add-update-preview .el-textarea /deep/ .el-textarea__inner {
				border: 1px solid #B1DBE0;
				border-radius: 0px;
				padding: 12px;
				color: #85B3B9;
				background: #fff;
				width: 100%;
				font-size: 14px;
				min-height: 150px;
				height: auto;
			}
	
	.add-update-preview .btn3 {
				border: 2px solid #02A79C;
				cursor: pointer;
				border-radius: 4px;
				padding: 0 10px;
				margin: 0 10px 0 0;
				color: #02A79C;
				background: none;
				width: auto;
				font-size: 16px;
				min-width: 110px;
				height: 40px;
			}
	
	.add-update-preview .btn3:hover {
				opacity: 0.8;
			}
	
	.editor>.avatar-uploader {
		line-height: 0;
		height: 0;
	}
</style>
