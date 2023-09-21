from django.shortcuts import render
import bankApp.models as bm
import random


# Create your views here.
#dashboard
def board(request):
     return render(request,'custTemp/cust_board.html')

def deposit(request,account=None):
     print("deposit in=",account)
     if request.method == 'POST':
          dep_amount1=request.POST['deposit']
          ts_id1=random.randint(10000,1000000)
          status=True
          print("depositAmount=",dep_amount1,account)
          #Master details
          master_data=bm.Master_Account.objects.get(account_no_id=account)
          master_bal=master_data.master_balance
          print("Master_Balance=",master_bal)
          updated_bal=int(dep_amount1)+master_bal


          ob=bm.Account_Info.objects.create(ts_id=ts_id1,account_no_id=account,deposit_amount=dep_amount1,ts_st=True)
          ob.save()


          #master update

          master_row=bm.Master_Account.objects.get(account_no_id=account)
          master_row.deposit_amount=dep_amount1
          master_row.master_balance=updated_bal
          master_row.save()
          print("Transaction complted successfully")

     return render(request,'custTemp/deposit.html')

def withdraw(request,account=None):
     print("withdraw in=",account)
     if request.method == 'POST':
          with_amount1=request.POST['withdraw']
          ts_id1=random.randint(10000,1000000)
          status=True
          print("withdrawAmount=",with_amount1,account)
          #Master details
          master_data=bm.Master_Account.objects.get(account_no_id=account)
          master_bal=master_data.master_balance
          print("Master_Balance=",master_bal)
          updated_bal=master_bal-int(with_amount1)


          ob=bm.Account_Info.objects.create(ts_id=ts_id1,account_no_id=account,withdraw_amount=with_amount1,ts_st=True)
          ob.save()


          #master update

          master_row=bm.Master_Account.objects.get(account_no_id=account)
          master_row.withdraw_amount=with_amount1
          master_row.master_balance=updated_bal
          master_row.save()
          print("Transaction complted successfully")

          
     return render(request,'custTemp/withdraw.html')

def checkbal(request,account=None):
     print("check balance=",account)
     
          #Master details
     master_data=bm.Master_Account.objects.get(account_no_id=account)
     master_bal=master_data.master_balance
     print("Master_Balance=",master_bal)
     bal={'bal':master_bal}     


          #master update


     return render(request,'custTemp/check_balance.html',bal)