from flask import *
from database import*
import uuid

admin=Blueprint('admin',__name__)

@admin.route('/admin_home')
def admin_home():
	return render_template("admin_home.html")

@admin.route('/admin_view_customers',methods=['get','post'])
def admin_view_customers():
	data={}
	q="SELECT * FROM `customer`"
	data['view']=select(q)
	return render_template("admin_view_customers.html",data=data)


@admin.route('/admin_manage_contractor',methods=['get','post'])
def admin_manage_contractor():
	data={}
	q="SELECT * FROM `contractor` INNER JOIN `login` USING(`login_id`) "
	data['view']=select(q)

	if 'action' in request.args:
		action=request.args['action']
		con_id=request.args['con_id']
		log_id=request.args['log_id']
	else:
		action=None
	if action=='accept':
		q="UPDATE `login` SET `usertype`='contractor' WHERE `login_id`='%s'"%(log_id)
		update(q)
		flash("Update Usertype successfully....!")
		return redirect(url_for('admin.admin_manage_contractor'))
	if action=='reject':
		q="DELETE FROM `contractor` WHERE `contractor_id`='%s'"%(con_id)
		delete(q)
		q="DELETE FROM `login` WHERE `login_id`='%s'"%(log_id)
		delete(q)
		flash("Are You Sure....??")
		return redirect(url_for('admin.admin_manage_contractor'))
	return render_template("admin_manage_contractor.html",data=data)



@admin.route('/admin_view_feedback',methods=['get','post'])
def admin_view_feedback():
	data={}
	q="SELECT * FROM `feedback` INNER JOIN `customer` USING(`customer_id`)"
	data['view']=select(q)
	
	return render_template('admin_view_feedback.html',data=data)





