# -*- coding: utf-8 -*-
from openerp.osv import osv, fields


class amos_meeting3(osv.osv):
    # def total_price(self, cr, uid, ids, field_name, arg, context=None):
    #	res = {}
    #	for line in self.browse(cr, uid, ids, context=context):
    #		total_price = line.row*line.price
    #	return res
    #  def total_price(self, cr, uid, ids, field_name, args, context=None):
    #	res={}

    #	return res

    _name = 'amos.meeting3'
    _description = 'amos.meeting3'
    _columns = {
        'name': fields.char(u'标题', size=10, required=True, help=u'输入标题'),
        'boolean': fields.boolean('boolean'),
        'binary': fields.binary('binary'),  #'function':fields.function(type='float',method=True),
        'user_id': fields.many2one('res.users', u'帐号'),
        'price': fields.float(u'单价'),
        'state': fields.selection([('draft', 'Draft'), ('confirmed', 'Confirmed')], u'状态'),
        #'total_price':fields.function(total_price,store=True),


        'amos_partner': fields.many2many('res.partner', 'amos_meeting_rel', 'a_id', 'b_id', u'合作伙伴'),
        'amos_tags': fields.many2many('res.partner.category', 'amos_meeting_category_rel', 'a_id', 'b_id', u'标签'),

        'start_date': fields.date(u'开始日期'),
        'row': fields.integer(u'到会人数'),
        'note': fields.text(u'备注'),
        'product_id': fields.many2one('product.product', u'产品', required=True, domain=[('sale_ok', '=', True)]),
        'uom_id':fields.many2one('product.uom',u'单位'),
    }

    def onchange_product_id(self,cr,uid,ids,product_id,context=None):
        res={}
        print context,zhwl

        if product_id:
            product =self.pool.get('product.product').browse(cr,uid,product_id,context=context)
            res['name']=product.name
            res['uom_id']=product.uom_id.id
        return {'value':res}

        #   'product_id':fields.many2one('product.product',u'产品'),

        #  'product_id':fields.many2one('product.product',u'产品'),
        #    'product_id': fields.many2one('product.product', 'Product', domain=[('sale_ok', '=', True)], change_default=True, readonly=True, states={'draft': [('readonly', False)]}, ondelete='restrict'),







