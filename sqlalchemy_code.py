

### Simple filter
check = db.query(model_user.UserModel).filter(model_user.UserModel.id == result['user_id']).first()

## little complex 
all_data= db.query(model_user.Product.name,model_user.ANInventory.product_id, model_user.ANInventory.qty,
         model_user.ANInventory.created_by,model_user.ANInventory.contact_id).join(model_user.Product,
         model_user.ANInventory.product_id == model_user.Product.id).filter(model_user.ANInventory.contact_id == contact_id).all()
         

all_data= db.query(model_user.Product.name,model_user.ManagerInventory.user_id, model_user.ManagerInventory.product_id,
         model_user.ManagerInventory.qty).join(model_user.Product,
         model_user.Product.id ==model_user.ManagerInventory.product_id, isouter =True).all()
         
all_data= db.query(model_user.RequestedInventory.order_no,model_user.Status.name,
        array_agg(model_user.RequestedInventory.date.distinct()),model_user.RequestedInventory.status_id).join(model_user.Status, model_user.Status.id ==model_user.RequestedInventory.status_id,
        isouter =True).group_by(model_user.RequestedInventory.order_no,model_user.Status.name,model_user.RequestedInventory.status_id).filter(model_user.RequestedInventory.date == date,
        model_user.Status.name == status_).all()
        
        
all_order_no= db.query(model_user.Product.name,model_user.Status.name,
        model_user.RequestedInventory.qty, model_user.RequestedInventory.status_id).join(model_user.Status, model_user.Status.id ==model_user.RequestedInventory.status_id).join(
           model_user.Product, model_user.Product.id ==model_user.RequestedInventory.product_id
        ).filter(model_user.RequestedInventory.order_no == order_no).all()
        
        
