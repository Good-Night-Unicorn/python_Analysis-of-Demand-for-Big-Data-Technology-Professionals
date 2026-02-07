<template>
	<div :style='{"padding":"50px 20px 20px","background":"none"}'>
		<el-form
			:style='{"border":"1px solid #BFBFBF","padding":"42px  25% 42px  15%","margin":"0 auto","flexWrap":"wrap","background":"#fff","display":"flex"}'
			class="add-update-preview"
			ref="ruleForm"
			:rules="rules"
			:model="ruleForm"
			label-width="180px"
		>
			<el-form-item :style='{"border":"0px solid #eee","width":"100%","padding":"0","margin":"0 0 20px!important"}' label="原密码" prop="password">
				<el-input type="password" v-model="ruleForm.password" ></el-input>
			</el-form-item>
			<el-form-item :style='{"border":"0px solid #eee","width":"100%","padding":"0","margin":"0 0 20px!important"}' label="新密码" prop="newpassword">
				<el-input type="password" v-model="ruleForm.newpassword" ></el-input>
			</el-form-item>
			<el-form-item :style='{"border":"0px solid #eee","width":"100%","padding":"0","margin":"0 0 20px!important"}' label="确认密码" prop="repassword">
				<el-input type="password" v-model="ruleForm.repassword" ></el-input>
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
export default {
	data() {
		return {
			dialogVisible: false,
			ruleForm: {},
			user: {},
			rules: {
				password: [
					{
						required: true,
						message: "密码不能为空",
						trigger: "blur"
					}
				],
				newpassword: [
					{
						required: true,
						message: "新密码不能为空",
						trigger: "blur"
					}
				],
				repassword: [
					{
						required: true,
						message: "确认密码不能为空",
						trigger: "blur"
					}
				]
			}
		};
	},
	mounted() {
		this.$http({
			url: `${this.$storage.get("sessionTable")}/session`,
			method: "get"
		}).then(({ data }) => {
			if (data && data.code === 0) {
				this.user = data.data;
			} else {
				this.$message.error(data.msg);
			}
		});
	},
	methods: {
		onLogout() {
			this.$storage.remove("Token");
			this.$router.replace({ name: "login" });
		},
		// 修改密码
		async onUpdateHandler() {
			this.$refs["ruleForm"].validate(async valid => {
				if (valid) {
					var password = "";
					if (this.user.mima) {
						password = this.user.mima;
					} else if (this.user.password) {
						password = this.user.password;
					}
					if(this.$storage.get("sessionTable")=='users'){
						if (this.ruleForm.password != password) {
							this.$message.error("原密码错误");
							return;
						}
						if (this.ruleForm.newpassword != this.ruleForm.repassword) {
							this.$message.error("两次密码输入不一致");
							return;
						}
						this.user.password = this.ruleForm.newpassword;
						this.user.mima = this.ruleForm.newpassword;
						this.$http({
							url: `${this.$storage.get("sessionTable")}/update`,
							method: "post",
							data: this.user
						}).then(({ data }) => {
							if (data && data.code === 0) {
								this.$message({
									message: "修改密码成功,下次登录系统生效",
									type: "success",
									duration: 1500,
									onClose: () => {
									}
								});
							} else {
								this.$message.error(data.msg);
							}
						});
						return false
					}
					if (this.ruleForm.password != password) {
						this.$message.error("原密码错误");
						return;
					}
					if (this.ruleForm.newpassword != this.ruleForm.repassword) {
						this.$message.error("两次密码输入不一致");
						return;
					}
					if (this.ruleForm.newpassword == this.ruleForm.password) {
						this.$message.error("新密码与原密码相同");
						return;
					}
					this.user.password = this.ruleForm.newpassword;
					this.user.mima = this.ruleForm.newpassword;
					this.$http({
						url: `${this.$storage.get("sessionTable")}/update`,
						method: "post",
						data: this.user
					}).then(({ data }) => {
						if (data && data.code === 0) {
							this.$message({
								message: "修改密码成功,下次登录系统生效",
								type: "success",
								duration: 1500,
								onClose: () => {
								}
							});
						} else {
							this.$message.error(data.msg);
						}
					});
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
</style>
