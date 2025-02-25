from flask import * 
from database import * 

public=Blueprint('public',__name__)


@public.route('/')
def home():
	return render_template("home.html")


@public.route('/login',methods=['get','post'])
def login():
	if 'submit' in request.form:
		uname=request.form['uname']
		pwd=request.form['pwd']
		q="SELECT * FROM `login` WHERE `username`='%s' AND `password`='%s'"%(uname,pwd)
		res=select(q)
		if res:
			session['lid']=res[0]['login_id']
			if res[0]['usertype']=='admin':
				flash("login successfully....!")
				return redirect(url_for('admin.admin_home'))
			elif res[0]['usertype']=='contractor':
				q="select * from contractor where login_id='%s'"%(session['lid'])
				res=select(q)
				print(res)
				if res:
					session['con_id']=res[0]['contractor_id']
					flash("login successfully....!")
					return redirect(url_for('contractor.contractor_home'))
			elif res[0]['usertype']=='shop':
				q="select * from shop where login_id='%s'"%(session['lid'])
				res=select(q)
				print(res)
				if res:
					session['shop_id']=res[0]['shop_id']
					flash("login successfully....!")
					return redirect(url_for('shop.shop_home'))
		else:
			flash("INVALID USERNAME OR PASSWORD")
	return render_template("login.html")



@public.route('/contractor_registration',methods=['get','post'])
def contractor_registration():
	data={}
	if 'manage' in request.form:
		fname=request.form['fname']
		lname=request.form['lname']
		place=request.form['place']
		phone=request.form['phone']
		email=request.form['email']
		aadhar=request.form['aadhar']

		uname=request.form['uname']
		passw=request.form['passw']

		q="select * from login where username='%s' and password='%s'"%(uname,passw)
		res=select(q)
		if res:
			flash('THIS USER IS ALREADY EXIST')
		else:
			q="insert into login values(null,'%s','%s','pending')"%(uname,passw)
			lid=insert(q)
			q="insert into contractor values(NULL,'%s','%s','%s','%s','%s','%s','%s')"%(lid,fname,lname,place,phone,email,aadhar)
			insert(q)
			flash("Registration Request Send Successfully.....!")
			return redirect(url_for('public.login'))
	return render_template("contractor_registration.html",data=data)


@public.route('/shop_registration',methods=['get','post'])
def shop_registration():
	data={}
	if 'manage' in request.form:
		fname=request.form['fname']
		place=request.form['place']
		phone=request.form['phone']
		email=request.form['email']
		
		uname=request.form['uname']
		passw=request.form['passw']

		q="select * from login where username='%s' and password='%s'"%(uname,passw)
		res=select(q)
		if res:
			flash('THIS USER IS ALREADY EXIST')
		else:
			q="insert into login values(null,'%s','%s','shop')"%(uname,passw)
			lid=insert(q)
			q="insert into shop values(NULL,'%s','%s','%s','%s','%s')"%(lid,fname,place,phone,email)
			insert(q)
			flash("Registration Success....!")
			return redirect(url_for('public.login'))
	return render_template("shop_registration.html",data=data)