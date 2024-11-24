from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from models import CalculationResult, db
from forms import CalculationForm

main_bp = Blueprint('main', __name__)

@main_bp.route('/home', methods=['GET', 'POST'])
@login_required
def home():
    form = CalculationForm()
    if form.validate_on_submit():
        input1 = form.input1.data
        input2 = form.input2.data
        input3 = form.input3.data
        
        result = input1 + input2 + input3
        
        calculation = CalculationResult(input1=input1, input2=input2, input3=input3, result=result, user_id=current_user.id)
        db.session.add(calculation)
        db.session.commit()
        
        flash('Calculation successful!')
        return redirect(url_for('main.result', result=result))
    
    return render_template('home.html', form=form)

@main_bp.route('/result/<float:result>')
@login_required
def result(result):
    return render_template('result.html', result=result)