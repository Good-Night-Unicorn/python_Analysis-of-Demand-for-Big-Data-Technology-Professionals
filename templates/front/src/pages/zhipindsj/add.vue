<template>
	<div class="add-update-preview">
		<el-form
			class="add-update-form"
			ref="ruleForm"
			:model="ruleForm"
			:rules="rules"
			label-width="150px"
			>
			<el-form-item class="add-item" label="公司名称" prop="brandname">
				<el-input v-model="ruleForm.brandname" 
					placeholder="公司名称" clearable :disabled=" false  ||ro.brandname"></el-input>
			</el-form-item>
			<el-form-item class="add-item" label="职位名称" prop="jobname">
				<el-input v-model="ruleForm.jobname" 
					placeholder="职位名称" clearable :disabled=" false  ||ro.jobname"></el-input>
			</el-form-item>
			<el-form-item class="add-item" label="公司LOGO" v-if="type!='cross' || (type=='cross' && !ro.brandlogo)" prop="brandlogo">
				<file-upload
					tip="点击上传公司LOGO"
					action="file/upload"
					:limit="3"
					:multiple="true"
					:fileUrls="ruleForm.brandlogo?ruleForm.brandlogo:''"
					@change="brandlogoUploadChange"
					></file-upload>
			</el-form-item>
			<el-form-item class="add-item" v-else label="公司LOGO" prop="brandlogo">
				<img v-if="ruleForm.brandlogo.substring(0,4)=='http'" class="upload-img" v-bind:key="index" :src="ruleForm.brandlogo.split(',')[0]">
				<img v-else class="upload-img" v-bind:key="index" v-for="(item,index) in ruleForm.brandlogo.split(',')" :src="baseUrl+item">
			</el-form-item>
			<el-form-item class="add-item" label="城市" prop="cityname">
				<el-input v-model="ruleForm.cityname" 
					placeholder="城市" clearable :disabled=" false  ||ro.cityname"></el-input>
			</el-form-item>
			<el-form-item class="add-item" label="学历" prop="jobdegree">
				<el-input v-model="ruleForm.jobdegree" 
					placeholder="学历" clearable :disabled=" false  ||ro.jobdegree"></el-input>
			</el-form-item>
			<el-form-item class="add-item" label="工作经验" prop="jobexperience">
				<el-input v-model="ruleForm.jobexperience" 
					placeholder="工作经验" clearable :disabled=" false  ||ro.jobexperience"></el-input>
			</el-form-item>
			<el-form-item class="add-item" label="待遇描述" prop="salarydesc">
				<el-input v-model="ruleForm.salarydesc" 
					placeholder="待遇描述" clearable :disabled=" false  ||ro.salarydesc"></el-input>
			</el-form-item>
			<el-form-item class="add-item" label="公司类型" prop="brandIndustry">
				<el-input v-model="ruleForm.brandIndustry" 
					placeholder="公司类型" clearable :disabled=" false  ||ro.brandIndustry"></el-input>
			</el-form-item>
			<el-form-item class="add-item" label="公司规模" prop="brandscalename">
				<el-input v-model="ruleForm.brandscalename" 
					placeholder="公司规模" clearable :disabled=" false  ||ro.brandscalename"></el-input>
			</el-form-item>
			<el-form-item class="add-item" label="老板职务" prop="bosstitle">
				<el-input v-model="ruleForm.bosstitle" 
					placeholder="老板职务" clearable :disabled=" false  ||ro.bosstitle"></el-input>
			</el-form-item>
			<el-form-item class="add-item" label="福利" prop="welfarelist">
				<el-input
					type="textarea"
					:rows="8"
					placeholder="福利"
					v-model="ruleForm.welfarelist">
					</el-input>
			</el-form-item>
			<el-form-item class="add-item" label="技能要求" prop="skills">
				<el-input
					type="textarea"
					:rows="8"
					placeholder="技能要求"
					v-model="ruleForm.skills">
					</el-input>
			</el-form-item>
			<el-form-item class="add-item" label="详情地址" prop="detailurl">
				<el-input
					type="textarea"
					:rows="8"
					placeholder="详情地址"
					v-model="ruleForm.detailurl">
					</el-input>
			</el-form-item>

			<el-form-item class="add-btn-item">
				<el-button class="submitBtn"  type="primary" @click="onSubmit">
					<span class="icon iconfont icon-kaitongfuwu"></span>
					<span class="text">确定</span>
				</el-button>
				<el-button class="closeBtn" @click="back()">
					<span class="icon iconfont icon-shanchu1"></span>
					<span class="text">取消</span>
				</el-button>
			</el-form-item>
		</el-form>
	</div>
</template>

<script>
	export default {
		data() {
			return {
				id: '',
				baseUrl: '',
				ro:{
					brandname : false,
					jobname : false,
					brandlogo : false,
					cityname : false,
					jobdegree : false,
					jobexperience : false,
					salarydesc : false,
					brandIndustry : false,
					brandscalename : false,
					bosstitle : false,
					welfarelist : false,
					skills : false,
					detailurl : false,
					clicktime : false,
					storeupnum : false,
				},
				type: '',
				userTableName: localStorage.getItem('UserTableName'),
				ruleForm: {
					brandname: '',
					jobname: '',
					brandlogo: '',
					cityname: '',
					jobdegree: '',
					jobexperience: '',
					salarydesc: '',
					brandIndustry: '',
					brandscalename: '',
					bosstitle: '',
					welfarelist: '',
					skills: '',
					detailurl: '',
					clicktime: '',
					storeupnum: '',
				},


				rules: {
					brandname: [
					],
					jobname: [
					],
					brandlogo: [
					],
					cityname: [
					],
					jobdegree: [
					],
					jobexperience: [
					],
					salarydesc: [
					],
					brandIndustry: [
					],
					brandscalename: [
					],
					bosstitle: [
					],
					welfarelist: [
					],
					skills: [
					],
					detailurl: [
						{ validator: this.$validate.isURL, trigger: 'blur' },
					],
					clicktime: [
					],
					storeupnum: [
						{ validator: this.$validate.isIntNumer, trigger: 'blur' },
					],
				},
				centerType: false,
			};
		},
		computed: {



		},
		components: {
		},
		created() {
			if(this.$route.query.centerType){
				this.centerType = true
			}
			//this.bg();
			let type = this.$route.query.type ? this.$route.query.type : '';
			this.init(type);
			this.baseUrl = this.$config.baseUrl;
		},
		methods: {
			getMakeZero(s) {
				return s < 10 ? '0' + s : s;
			},
			// 下载
			download(file){
				window.open(`${file}`)
			},
			// 初始化
			init(type) {
				this.type = type;
				if(type=='cross'){
					var obj = JSON.parse(localStorage.getItem('crossObj'));
					for (var o in obj){
						if(o=='brandname'){
							this.ruleForm.brandname = obj[o];
							this.ro.brandname = true;
							continue;
						}
						if(o=='jobname'){
							this.ruleForm.jobname = obj[o];
							this.ro.jobname = true;
							continue;
						}
						if(o=='brandlogo'){
							this.ruleForm.brandlogo = obj[o]?obj[o].split(",")[0]:'';
							this.ro.brandlogo = true;
							continue;
						}
						if(o=='cityname'){
							this.ruleForm.cityname = obj[o];
							this.ro.cityname = true;
							continue;
						}
						if(o=='jobdegree'){
							this.ruleForm.jobdegree = obj[o];
							this.ro.jobdegree = true;
							continue;
						}
						if(o=='jobexperience'){
							this.ruleForm.jobexperience = obj[o];
							this.ro.jobexperience = true;
							continue;
						}
						if(o=='salarydesc'){
							this.ruleForm.salarydesc = obj[o];
							this.ro.salarydesc = true;
							continue;
						}
						if(o=='brandIndustry'){
							this.ruleForm.brandIndustry = obj[o];
							this.ro.brandIndustry = true;
							continue;
						}
						if(o=='brandscalename'){
							this.ruleForm.brandscalename = obj[o];
							this.ro.brandscalename = true;
							continue;
						}
						if(o=='bosstitle'){
							this.ruleForm.bosstitle = obj[o];
							this.ro.bosstitle = true;
							continue;
						}
						if(o=='welfarelist'){
							this.ruleForm.welfarelist = obj[o];
							this.ro.welfarelist = true;
							continue;
						}
						if(o=='skills'){
							this.ruleForm.skills = obj[o];
							this.ro.skills = true;
							continue;
						}
						if(o=='detailurl'){
							this.ruleForm.detailurl = obj[o];
							this.ro.detailurl = true;
							continue;
						}
						if(o=='clicktime'){
							this.ruleForm.clicktime = obj[o];
							this.ro.clicktime = true;
							continue;
						}
						if(o=='storeupnum'){
							this.ruleForm.storeupnum = obj[o];
							this.ro.storeupnum = true;
							continue;
						}
					}
				}else if(type=='edit'){
					this.info()
				}

				if (localStorage.getItem('raffleType') && localStorage.getItem('raffleType') != null) {
					localStorage.removeItem('raffleType')
					setTimeout(() => {
						this.onSubmit()
					}, 300)
				}
			},

			// 多级联动参数
			// 多级联动参数
			info() {
				this.$http.get(`zhipindsj/detail/${this.$route.query.id}`, {emulateJSON: true}).then(res => {
					if (res.data.code == 0) {
						this.ruleForm = res.data.data;
					}
				});
			},
			// 提交
			async onSubmit() {
				if(!this.ruleForm.id) {
					delete this.ruleForm.userid
				}
				await this.$refs["ruleForm"].validate(async valid => {
					if(valid) {
						if(this.type=='cross'){
							var statusColumnName = localStorage.getItem('statusColumnName');
							var statusColumnValue = localStorage.getItem('statusColumnValue');
							if(statusColumnName && statusColumnName!='') {
								var obj = JSON.parse(localStorage.getItem('crossObj'));
								if(!statusColumnName.startsWith("[")) {
									for (var o in obj){
										if(o==statusColumnName){
											obj[o] = statusColumnValue;
										}
									}
									var table = localStorage.getItem('crossTable');
									await this.$http.post(table+'/update', obj).then(res => {});
								}
							}
						}


						await this.$http.post(`zhipindsj/${this.ruleForm.id?'update':this.centerType?'save':'add'}`, this.ruleForm).then(async res => {
							if (res.data.code == 0) {
								this.$message({
									message: '操作成功',
									type: 'success',
									duration: 1500,
									onClose: () => {
										this.$router.go(-1);
										
									}
								});
							} else {
								this.$message({
									message: res.data.msg,
									type: 'error',
									duration: 1500
								});
							}
						});
					}
				});
			},
			// 获取uuid
			getUUID () {
				return new Date().getTime();
			},
			// 返回
			back() {
				this.$router.go(-1);
			},
			brandlogoUploadChange(fileUrls) {
				this.ruleForm.brandlogo = fileUrls.replace(new RegExp(this.$config.baseUrl,"g"),"");
			},
		}
	};
</script>

<style rel="stylesheet/scss" lang="scss" scoped>
	.add-update-preview {
		padding: 20px 16%;
		margin: 0px auto;
		background: #F2F3F7;
		width: 100%;
		position: relative;
		.add-update-form {
			width: 100%;
			position: relative;
			.add-item.el-form-item {
				padding: 10px;
				margin: 0 0 10px;
				background: none;
				display: inline-block;
				width: 48%;
				/deep/ .el-form-item__label {
					padding: 0 10px 0 0;
					color: #666;
					font-weight: 500;
					width: 150px;
					font-size: 14px;
					line-height: 40px;
					text-align: center;
				}
				/deep/ .el-form-item__content {
					margin-left: 150px;
				}
				.el-input {
					width: 100%;
				}
				.el-input /deep/ .el-input__inner {
					border: 1px solid #E2E3E5;
					border-radius: 0;
					padding: 0 12px;
					box-shadow: 0 0 0px rgba(64, 158, 255, .5);
					outline: none;
					color: #000;
					width: 80%;
					font-size: 15px;
					height: 40px;
				}
				.el-input /deep/ .el-input__inner[readonly="readonly"] {
					border: 1px solid #E2E3E5;
					cursor: not-allowed;
					border-radius: 0;
					padding: 0 12px;
					box-shadow: 0 0 0px rgba(85, 85, 127, 0.5);
					outline: none;
					color: #000;
					background: #f8f8f8;
					width: 80%;
					font-size: 15px;
					height: 40px;
				}
				.el-input-number /deep/ .el-input__inner {
					text-align: left;
					border: 1px solid #E2E3E5;
					border-radius: 0;
					padding: 0 12px;
					box-shadow: 0 0 0px rgba(64, 158, 255, .5);
					outline: none;
					color: #000;
					width: 80%;
					font-size: 15px;
					height: 40px;
				}
				.el-input-number /deep/ .is-disabled .el-input__inner {
					text-align: left;
					border: 1px solid #E2E3E5;
					cursor: not-allowed;
					border-radius: 0;
					padding: 0 12px;
					box-shadow: 0 0 0px rgba(85, 85, 127, 0.5);
					outline: none;
					color: #000;
					background: #f8f8f8;
					width: 80%;
					font-size: 15px;
					height: 40px;
				}
				.el-input-number /deep/ .el-input-number__decrease {
					display: none;
				}
				.el-input-number /deep/ .el-input-number__increase {
					display: none;
				}
				.el-select {
					width: 80%;
				}
				.el-select /deep/ .el-input__inner {
					border: 1px solid #E2E3E5;
					border-radius: 0;
					padding: 0 10px;
					box-shadow: 0 0 0px rgba(64, 158, 255, .5);
					outline: none;
					color: #000;
					width: 100%;
					font-size: 15px;
					height: 40px;
				}
				.el-select /deep/ .is-disabled .el-input__inner {
					border: 1px solid #E2E3E5;
					cursor: not-allowed;
					border-radius: 0;
					padding: 0 10px;
					box-shadow: 0 0 0px rgba(85, 85, 127, 0.5);
					outline: none;
					color: #000;
					background: #f8f8f8;
					width: 100%;
					font-size: 15px;
					height: 40px;
				}
				.el-date-editor {
					width: 80%;
				}
				.el-date-editor /deep/ .el-input__inner {
					border: 1px solid #E2E3E5;
					border-radius: 0;
					padding: 0 10px 0 30px;
					box-shadow: 0 0 0px rgba(64, 158, 255, .5);
					outline: none;
					color: #000;
					width: 100%;
					font-size: 15px;
					height: 40px;
				}
				.el-date-editor /deep/ .el-input__inner[readonly="readonly"] {
					border: 1px solid #E2E3E5;
					cursor: not-allowed;
					border-radius: 0;
					padding: 0 10px 0 30px;
					box-shadow: 0 0 0px rgba(85, 85, 127, 0.5);
					outline: none;
					color: #000;
					background: #f8f8f8;
					width: 100%;
					font-size: 15px;
					height: 40px;
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
					border: 1px dashed #999;
					cursor: pointer;
					border-radius: 6px;
					color: #999;
					width: 100px;
					font-size: 32px;
					line-height: 100px;
					text-align: center;
					height: 100px;
				}
				/deep/ .el-upload-list .el-upload-list__item {
					border: 1px dashed #999;
					cursor: pointer;
					border-radius: 6px;
					color: #999;
					width: 100px;
					font-size: 32px;
					line-height: 100px;
					text-align: center;
					height: 100px;
					font-size: 14px;
					line-height: 1.8;
				}
				/deep/ .el-upload .el-icon-plus {
					border: 1px dashed #999;
					cursor: pointer;
					border-radius: 6px;
					color: #999;
					width: 100px;
					font-size: 32px;
					line-height: 100px;
					text-align: center;
					height: 100px;
				}
				/deep/ .el-upload__tip {
					color: #838fa1;
					display: none;
				}
				.el-textarea /deep/ .el-textarea__inner {
					border: 1px solid #E2E3E5;
					border-radius: 0;
					padding: 12px;
					box-shadow: 0 0 0px rgba(64, 158, 255, .5);
					outline: none;
					color: #000;
					width: 80%;
					font-size: 14px;
					height: 120px;
				}
				.el-textarea /deep/ .el-textarea__inner[readonly="readonly"] {
					border: 1px solid #E2E3E5;
					cursor: not-allowed;
					border-radius: 4px;
					padding: 12px;
					box-shadow: 0 0 0px rgba(85, 85, 127, 0.5);
					outline: none;
					color: #000;
					background: #f8f8f8;
					width: 80%;
					font-size: 14px;
					height: 120px;
				}
				/deep/ .el-input__inner::placeholder {
					color: #999;
					font-size: 14px;
				}
				/deep/ textarea::placeholder {
					color: #999;
					font-size: 14px;
				}
				.editor {
					background-color: #fff;
					border-radius: 0;
					padding: 0;
					box-shadow: 0 0 0px rgba(75,223,201,.5);
					margin: 0;
					width: 80%;
					border-color: #ccc;
					border-width: 0;
					border-style: solid;
					height: auto;
				}
				.upload-img {
					width: 100px;
					height: 100px;
				}
				.viewBtn {
					border: 0;
					cursor: pointer;
					padding: 0 10px;
					margin: 0;
					color: #fff;
					display: inline-block;
					font-size: 14px;
					line-height: 30px;
					border-radius: 4px;
					outline: none;
					background: #5AC3B2;
					width: auto;
					height: 30px;
				}
				.viewBtn:hover {
					color: #fff;
					background: #5AC3B290;
				}
				.unviewBtn {
					border: 0;
					cursor: not-allowed;
					padding: 0 10px;
					margin: 0;
					color: #ccc;
					display: inline-block;
					font-size: 14px;
					line-height: 30px;
					border-radius: 4px;
					outline: none;
					background: #858585;
					width: auto;
					height: 30px;
				}
				.unviewBtn:hover {
					color: #ccc;
					background: #858585;
				}
			}
			.add-btn-item {
				padding: 0;
				margin: 0;
				.submitBtn {
					border: 0;
					cursor: pointer;
					border-radius: 4px;
					padding: 0 15px;
					margin: 0 20px 0 0;
					outline: none;
					background: #5AC3B2;
					display: inline-block;
					width: auto;
					font-size: 14px;
					line-height: 30px;
					height: 30px;
					.icon {
						color: rgba(255, 255, 255, 1);
						display: none;
					}
					.text {
						color: rgba(255, 255, 255, 1);
					}
				}
				.submitBtn:hover {
					background: #5AC3B290;
					.icon {
						color: #fff;
					}
					.text {
						color: #fff;
					}
				}
				.closeBtn {
					border: 0px solid rgba(64, 158, 255, 1);
					cursor: pointer;
					padding: 0 15px;
					margin: 0 20px 0 0;
					display: inline-block;
					font-size: 14px;
					line-height: 30px;
					border-radius: 4px;
					outline: none;
					background: #858585;
					width: auto;
					text-align: center;
					min-width: 100px;
					height: 30px;
					.icon {
						color: #fff;
						display: none;
					}
					.text {
						color: #fff;
					}
				}
				.closeBtn:hover {
					background: #85858590;
					.icon {
						color: #fff;
					}
					.text {
						color: #fff;
					}
				}
			}
		}
	}
	.el-date-editor.el-input {
		width: auto;
	}
</style>
