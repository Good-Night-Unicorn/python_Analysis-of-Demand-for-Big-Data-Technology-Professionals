<template>
	<div class="addEdit-block">
		<el-form
			class="add-update-preview"
			ref="ruleForm"
			:model="ruleForm"
			:rules="rules"
			label-width="180px"
		>
			<template >
				<el-form-item class="input" v-if="type!='info'"  label="公司名称" prop="brandname" >
					<el-input v-model="ruleForm.brandname" placeholder="公司名称" clearable  :readonly="ro.brandname"></el-input>
				</el-form-item>
				<el-form-item v-else class="input" label="公司名称" prop="brandname" >
					<el-input v-model="ruleForm.brandname" placeholder="公司名称" readonly></el-input>
				</el-form-item>
				<el-form-item class="input" v-if="type!='info'"  label="职位名称" prop="jobname" >
					<el-input v-model="ruleForm.jobname" placeholder="职位名称" clearable  :readonly="ro.jobname"></el-input>
				</el-form-item>
				<el-form-item v-else class="input" label="职位名称" prop="jobname" >
					<el-input v-model="ruleForm.jobname" placeholder="职位名称" readonly></el-input>
				</el-form-item>
				<el-form-item class="upload" v-if="type!='info' && !ro.brandlogo" label="公司LOGO" prop="brandlogo" >
					<file-upload
						tip="点击上传公司LOGO"
						action="file/upload"
						:limit="3"
						:multiple="true"
						:fileUrls="ruleForm.brandlogo?ruleForm.brandlogo:''"
						@change="brandlogoUploadChange"
					></file-upload>
				</el-form-item>
				<el-form-item class="upload" v-else-if="ruleForm.brandlogo" label="公司LOGO" prop="brandlogo" >
					<img v-if="ruleForm.brandlogo.substring(0,4)=='http'&&ruleForm.brandlogo.split(',w').length>1" class="upload-img" style="margin-right:20px;" v-bind:key="index" :src="ruleForm.brandlogo" width="100" height="100">
					<img v-else-if="ruleForm.brandlogo.substring(0,4)=='http'" class="upload-img" style="margin-right:20px;" v-bind:key="index" :src="ruleForm.brandlogo.split(',')[0]" width="100" height="100">
					<img v-else class="upload-img" style="margin-right:20px;" v-bind:key="index" v-for="(item,index) in ruleForm.brandlogo.split(',')" :src="$base.url+item" width="100" height="100">
				</el-form-item>
				<el-form-item class="input" v-if="type!='info'"  label="城市" prop="cityname" >
					<el-input v-model="ruleForm.cityname" placeholder="城市" clearable  :readonly="ro.cityname"></el-input>
				</el-form-item>
				<el-form-item v-else class="input" label="城市" prop="cityname" >
					<el-input v-model="ruleForm.cityname" placeholder="城市" readonly></el-input>
				</el-form-item>
				<el-form-item class="input" v-if="type!='info'"  label="学历" prop="jobdegree" >
					<el-input v-model="ruleForm.jobdegree" placeholder="学历" clearable  :readonly="ro.jobdegree"></el-input>
				</el-form-item>
				<el-form-item v-else class="input" label="学历" prop="jobdegree" >
					<el-input v-model="ruleForm.jobdegree" placeholder="学历" readonly></el-input>
				</el-form-item>
				<el-form-item class="input" v-if="type!='info'"  label="工作经验" prop="jobexperience" >
					<el-input v-model="ruleForm.jobexperience" placeholder="工作经验" clearable  :readonly="ro.jobexperience"></el-input>
				</el-form-item>
				<el-form-item v-else class="input" label="工作经验" prop="jobexperience" >
					<el-input v-model="ruleForm.jobexperience" placeholder="工作经验" readonly></el-input>
				</el-form-item>
				<el-form-item class="input" v-if="type!='info'"  label="待遇描述" prop="salarydesc" >
					<el-input v-model="ruleForm.salarydesc" placeholder="待遇描述" clearable  :readonly="ro.salarydesc"></el-input>
				</el-form-item>
				<el-form-item v-else class="input" label="待遇描述" prop="salarydesc" >
					<el-input v-model="ruleForm.salarydesc" placeholder="待遇描述" readonly></el-input>
				</el-form-item>
				<el-form-item class="input" v-if="type!='info'"  label="公司类型" prop="brandIndustry" >
					<el-input v-model="ruleForm.brandIndustry" placeholder="公司类型" clearable  :readonly="ro.brandIndustry"></el-input>
				</el-form-item>
				<el-form-item v-else class="input" label="公司类型" prop="brandIndustry" >
					<el-input v-model="ruleForm.brandIndustry" placeholder="公司类型" readonly></el-input>
				</el-form-item>
				<el-form-item class="input" v-if="type!='info'"  label="公司规模" prop="brandscalename" >
					<el-input v-model="ruleForm.brandscalename" placeholder="公司规模" clearable  :readonly="ro.brandscalename"></el-input>
				</el-form-item>
				<el-form-item v-else class="input" label="公司规模" prop="brandscalename" >
					<el-input v-model="ruleForm.brandscalename" placeholder="公司规模" readonly></el-input>
				</el-form-item>
				<el-form-item class="input" v-if="type!='info'"  label="老板职务" prop="bosstitle" >
					<el-input v-model="ruleForm.bosstitle" placeholder="老板职务" clearable  :readonly="ro.bosstitle"></el-input>
				</el-form-item>
				<el-form-item v-else class="input" label="老板职务" prop="bosstitle" >
					<el-input v-model="ruleForm.bosstitle" placeholder="老板职务" readonly></el-input>
				</el-form-item>
			</template>
			<el-form-item class="textarea" v-if="type!='info'" label="福利" prop="welfarelist" >
				<el-input
					style="min-width: 200px; max-width: 600px;"
					type="textarea"
					:rows="8"
					placeholder="福利"
					v-model="ruleForm.welfarelist" >
				</el-input>
			</el-form-item>
			<el-form-item v-else-if="ruleForm.welfarelist" label="福利" prop="welfarelist" >
				<span class="text">{{ruleForm.welfarelist}}</span>
			</el-form-item>
			<el-form-item class="textarea" v-if="type!='info'" label="技能要求" prop="skills" >
				<el-input
					style="min-width: 200px; max-width: 600px;"
					type="textarea"
					:rows="8"
					placeholder="技能要求"
					v-model="ruleForm.skills" >
				</el-input>
			</el-form-item>
			<el-form-item v-else-if="ruleForm.skills" label="技能要求" prop="skills" >
				<span class="text">{{ruleForm.skills}}</span>
			</el-form-item>
			<el-form-item class="textarea" v-if="type!='info'" label="详情地址" prop="detailurl" >
				<el-input
					style="min-width: 200px; max-width: 600px;"
					type="textarea"
					:rows="8"
					placeholder="详情地址"
					v-model="ruleForm.detailurl" >
				</el-input>
			</el-form-item>
			<el-form-item v-else-if="ruleForm.detailurl" label="详情地址" prop="detailurl" >
				<span class="text">{{ruleForm.detailurl}}</span>
			</el-form-item>
			<el-form-item class="btn">
				<el-button class="btn3"  v-if="type!='info'" type="success" @click="onSubmit">
					<span class="icon iconfont icon-xihuan"></span>
					提交
				</el-button>
				<el-button class="btn4" v-if="type!='info'" type="success" @click="back()">
					<span class="icon iconfont icon-xihuan"></span>
					取消
				</el-button>
				<el-button class="btn5" v-if="type=='info'" type="success" @click="back()">
					<span class="icon iconfont icon-xihuan"></span>
					返回
				</el-button>
			</el-form-item>
		</el-form>
    

	</div>
</template>
<script>
	import { 
		isIntNumer,
		isURL,
	} from "@/utils/validate";
	export default {
		data() {
			var validateUrl = (rule, value, callback) => {
				if(!value){
					callback();
				} else if (!isURL(value)) {
					callback(new Error("请输入正确的URL地址"));
				} else {
					callback();
				}
			};
			var validateIntNumber = (rule, value, callback) => {
				if(!value){
					callback();
				} else if (!isIntNumer(value)) {
					callback(new Error("请输入整数"));
				} else {
					callback();
				}
			};
			return {
				id: '',
				type: '',
			
			
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
						{ validator: validateUrl, trigger: 'blur' },
					],
					clicktime: [
					],
					storeupnum: [
						{ validator: validateIntNumber, trigger: 'blur' },
					],
				},
			};
		},
		props: ["parent"],
		computed: {



		},
		components: {
		},
		created() {
		},
		methods: {
			// 下载
			download(file){
				window.open(`${file}`)
			},
			// 初始化
			init(id,type) {
				if (id) {
					this.id = id;
					this.type = type;
				}
				if(this.type=='info'||this.type=='else'||this.type=='msg'){
					this.info(id);
				}else if(this.type=='logistics'){
					for(let x in this.ro) {
						this.ro[x] = true
					}
					this.logistics=false;
					this.info(id);
				}else if(this.type=='cross'){
					var obj = this.$storage.getObj('crossObj');
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
							this.ruleForm.brandlogo = obj[o];
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
				}
			
			},
			// 多级联动参数

			info(id) {
				this.$http({
					url: `zhipindsj/info/${id}`,
					method: "get"
				}).then(({ data }) => {
					if (data && data.code === 0) {
						this.ruleForm = data.data;
						//解决前台上传图片后台不显示的问题
						let reg=new RegExp('../../../upload','g')//g代表全部
					} else {
						this.$message.error(data.msg);
					}
				});
			},

			// 提交
			async onSubmit() {
					if(this.ruleForm.brandlogo!=null) {
						this.ruleForm.brandlogo = this.ruleForm.brandlogo.replace(new RegExp(this.$base.url,"g"),"");
					}
					var objcross = this.$storage.getObj('crossObj');
					if(!this.ruleForm.id) {
						delete this.ruleForm.userid
					}
					await this.$refs["ruleForm"].validate(async valid => {
						if (valid) {
							if(this.type=='cross'){
								var statusColumnName = this.$storage.get('statusColumnName');
								var statusColumnValue = this.$storage.get('statusColumnValue');
								if(statusColumnName!='') {
									var obj = this.$storage.getObj('crossObj');
									if(statusColumnName && !statusColumnName.startsWith("[")) {
										for (var o in obj){
											if(o==statusColumnName){
												obj[o] = statusColumnValue;
											}
										}
										var table = this.$storage.get('crossTable');
										await this.$http({
											url: `${table}/update`,
											method: "post",
											data: obj
										}).then(({ data }) => {});
									}
								}
							}
							
							await this.$http({
								url: `zhipindsj/${!this.ruleForm.id ? "save" : "update"}`,
								method: "post",
								data: this.ruleForm
							}).then(async ({ data }) => {
								if (data && data.code === 0) {
									this.$message({
										message: "操作成功",
										type: "success",
										duration: 1500,
										onClose: () => {
											this.parent.showFlag = true;
											this.parent.addOrUpdateFlag = false;
											this.parent.zhipindsjCrossAddOrUpdateFlag = false;
											this.parent.search();
											this.parent.contentStyleChange();
										}
									});
								} else {
									this.$message.error(data.msg);
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
				this.parent.showFlag = true;
				this.parent.addOrUpdateFlag = false;
				this.parent.zhipindsjCrossAddOrUpdateFlag = false;
				this.parent.contentStyleChange();
			},
			brandlogoUploadChange(fileUrls) {
				this.ruleForm.brandlogo = fileUrls;
			},
		}
	};
</script>
<style lang="scss" scoped>
	.addEdit-block {
		padding: 50px 20px 20px;
		background: none;
	}
	.add-update-preview {
		border: 1px solid #BFBFBF;
		padding: 42px  25% 42px  15%;
		margin: 0 auto;
		background: #fff;
		display: flex;
		flex-wrap: wrap;
	}
	.amap-wrapper {
		width: 100%;
		height: 500px;
	}
	
	.search-box {
		position: absolute;
	}
	
	.el-date-editor.el-input {
		width: auto;
	}
	.add-update-preview /deep/ .el-form-item {
		border: 0px solid #eee;
		padding: 0;
		margin: 0 0 20px!important;
		width: 100%;
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
	.add-update-preview .el-form-item span.text {
		border: 1px solid #85B3B9;
		cursor: pointer;
		padding: 10px;
		margin: 0 0px 0 0;
		color: #85B3B9;
		font-weight: 400;
		display: block;
		font-size: 14px;
		line-height: 24px;
		border-radius: 0px;
		background: #fff;
		width: 100%;
		text-align: left;
		height: auto;
	}
	
	.add-update-preview .el-input {
		width: 100%;
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
	.add-update-preview .el-input /deep/ .el-input__inner[readonly="readonly"] {
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
	.add-update-preview .el-input-number {
		text-align: left;
		width: 100%;
	}
	.add-update-preview .el-input-number /deep/ .el-input__inner {
		text-align: left;
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
	.add-update-preview .el-input-number /deep/ .is-disabled .el-input__inner {
		text-align: left;
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
	.add-update-preview .el-input-number /deep/ .el-input-number__decrease {
		display: none;
	}
	.add-update-preview .el-input-number /deep/ .el-input-number__increase {
		display: none;
	}
	.add-update-preview .el-select {
		width: 100%;
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
	.add-update-preview .el-select /deep/ .is-disabled .el-input__inner {
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
	.add-update-preview .el-date-editor {
		width: 100%;
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
	.add-update-preview .el-date-editor /deep/ .el-input__inner[readonly="readonly"] {
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
	.add-update-preview .viewBtn {
		border: 1px solid #85B3B9;
		cursor: pointer;
		padding: 0 15px;
		margin: 0 20px 0 0;
		color: #85B3B9;
		font-weight: 400;
		font-size: 14px;
		line-height: 40px;
		border-radius: 0px;
		background: #fff;
		width: 100%;
		text-align: left;
		height: 40px;
		.iconfont {
			margin: 0 2px;
			color: #85B3B9;
			font-size: 14px;
			height: 70px;
		}
	}
	.add-update-preview .viewBtn:hover {
		opacity: 0.8;
	}
	.add-update-preview .downBtn {
		border: 1px solid #85B3B9;
		cursor: pointer;
		padding: 0 15px;
		margin: 0 20px 0 0;
		color: #85B3B9;
		font-weight: 400;
		font-size: 14px;
		line-height: 40px;
		border-radius: 0px;
		background: #fff;
		width: 100%;
		text-align: left;
		height: 40px;
		.iconfont {
			margin: 0 2px;
			color: #85B3B9;
			font-size: 14px;
			height: 70px;
		}
	}
	.add-update-preview .downBtn:hover {
		opacity: 0.8;
	}
	.add-update-preview .unBtn {
		border: 1px solid #85B3B9;
		cursor: pointer;
		padding: 0 15px;
		margin: 0 20px 0 0;
		color: #85B3B9;
		font-weight: 400;
		font-size: 14px;
		line-height: 44px;
		border-radius: 0px;
		background: #fff;
		width: 100%;
		text-align: left;
		height: 44px;
		.iconfont {
			margin: 0 2px;
			color: #fff;
			display: none;
			font-size: 14px;
			height: 34px;
		}
	}
	.add-update-preview .unBtn:hover {
		opacity: 0.8;
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
	
	.add-update-preview /deep/ .upload .upload-img {
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
	.add-update-preview /deep/ .el-upload__tip {
		color: #666;
		white-space: nowrap;
		font-size: 14px;
		min-width: 100px;
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
	.add-update-preview .el-textarea /deep/ .el-textarea__inner[readonly="readonly"] {
				border: 1px solid #B1DBE0;
				border-radius: 0px;
				padding: 12px;
				color: #85B3B9;
				background: #fff;
				width: 100%;
				font-size: 14px;
				height: auto;
			}
	.add-update-preview .el-form-item.btn {
		padding: 0;
		margin: 30px 0;
		width: 100%;
		.btn1 {
			border: 0px solid #ccc;
			cursor: pointer;
			border-radius: 5px;
			padding: 0 10px;
			margin: 0 10px 0 0;
			color: #fff;
			background: #02A79C;
			width: auto;
			font-size: 16px;
			min-width: 110px;
			height: 40px;
			.iconfont {
				margin: 0 2px;
				color: #fff;
				display: none;
				font-size: 14px;
				height: 40px;
			}
		}
		.btn1:hover {
			opacity: 0.8;
		}
		.btn2 {
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
			.iconfont {
				margin: 0 2px;
				color: #fff;
				display: none;
				font-size: 14px;
				height: 34px;
			}
		}
		.btn2:hover {
			opacity: 0.8;
		}
		.btn3 {
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
			.iconfont {
				margin: 0 2px;
				color: #fff;
				display: none;
				font-size: 14px;
				height: 40px;
			}
		}
		.btn3:hover {
			opacity: 0.8;
		}
		.btn4 {
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
			.iconfont {
				margin: 0 2px;
				color: #fff;
				display: none;
				font-size: 14px;
				height: 40px;
			}
		}
		.btn4:hover {
			opacity: 0.8;
		}
		.btn5 {
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
			.iconfont {
				margin: 0 2px;
				color: #fff;
				display: none;
				font-size: 14px;
				height: 40px;
			}
		}
		.btn5:hover {
			opacity: 0.8;
		}
	}
</style>
