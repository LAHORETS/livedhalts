from odoo import models, fields, api,_
from odoo.exceptions import ValidationError, UserError


class document_sequence(models.Model):
    _inherit="documents.folder"
    _order = 'doc_seq asc'
    
    doc_seq= fields.Char(string="folder seq" ,copy=False)
    complete_seq =fields.Char(string="full seq" ,copy=False)
    
    
    def name_get(self):
        res = []
        for rec in self:
            res.append((rec.id, '%s . %s' % (rec.complete_seq , rec.name)))
        return res
    
    def get_sequence(self,record,parent_folder = False):
        if parent_folder:
            prev_rec = self.env['documents.folder'].search([('parent_folder_id','=',record.parent_folder_id.id)])
            prev_rec = prev_rec - record 
            all_seq =prev_rec.mapped('doc_seq')
            seq_val= [x for x in all_seq if x != False] 
            if len(seq_val) >0 :
                seq_val_nums = list(map(int, seq_val))
                seq_val_nums.sort()
                if len(str(seq_val_nums[-1]+1)) == 1:
                    new_seq= '0'+str(seq_val_nums[-1]+1)
                else:
                    new_seq= str(seq_val_nums[-1]+1)
#                 new_seq= '0'+str(seq_val_nums[-1]+1) 
                
                return new_seq
             
            else:
                new_seq ='01'
                return new_seq
 
        else:
            prev_docs = self.env['documents.folder'].search([('parent_folder_id','=',False)])
            if prev_docs:
                new_seq=''
                all_seq=prev_docs.mapped('doc_seq')
                seq_val= [x for x in all_seq if x != False]
                if len(seq_val) >0:
                    seq_val_nums = list(map(int, seq_val))
                    seq_val_nums.sort()
                    if len(str(seq_val_nums[-1]+1)) == 1:
                        new_seq= '0'+str(seq_val_nums[-1]+1)
                    else:
                        new_seq= str(seq_val_nums[-1]+1)
                else:
                    new_seq = '01'        
                return new_seq
    
    @api.model
    def create(self, vals):

        res= super(document_sequence,self).create(vals)
        
        if not res.parent_folder_id:
            fold_seq = self.get_sequence(res)
            res.doc_seq = fold_seq
            res.complete_seq = res.doc_seq

        elif res.parent_folder_id:
            fold_seq = self.get_sequence(res ,res.parent_folder_id)
            res.doc_seq = fold_seq
            res.complete_seq = str(res.parent_folder_id.complete_seq) +'.'+ res.doc_seq
        return res
    
    def write(self, vals):
        res = super(document_sequence, self).write(vals)
        if 'parent_folder_id' in vals:
            if not self.parent_folder_id:
                fold_seq = self.get_sequence(self)
                self.doc_seq = fold_seq
                self.complete_seq = self.doc_seq

            elif self.parent_folder_id:
                fold_seq = self.get_sequence(self ,self.parent_folder_id)
                self.doc_seq = fold_seq
                self.complete_seq = str(self.parent_folder_id.complete_seq) +'.'+ self.doc_seq
                
        return res

class DocumentAttachmentCustom(models.Model):
    _inherit="ir.attachment"  
    
    
#     @api.model_create_multi
#     def create(self, vals_list):
#         if 'name' in vals_list[0]:
#             prev_files = self.env['documents.document'].search([]).mapped('name')
#             if vals_list[0]['name'] in prev_files:
#                 raise UserError(_('file already existed'))
#             else:    
#                 res = super(DocumentAttachmentCustom , self).create(vals_list)
#                 return res
#             
        
        
        
class DocumentAttachmentDOC(models.Model):
    _inherit="documents.document"
    
    doc_seq=fields.Char('document sequence')
    doc_file_type=fields.Char('Type',compute="_compute_file_type")
    
    def _compute_file_type(self):
        for i in self:
            x=i.name.split(".")
            i.doc_file_type=x
    
    
    @api.onchange('folder_id')
    def onchange_folder_seq(self):
        if self.folder_id:
            if self.folder_id.complete_seq:
                self.doc_seq = self.folder_id.complete_seq
    
    
    
    def update_sequence(self):
        for rec in self:
            rec.onchange_folder_seq()
    
    
    
    @api.model
    def get_all_records(self):
        vehicle_type_name = []

        record=self.env['documents.document'].search([])
        for rec in record:
            vehicle_type_name.append(rec)
        # return record
        return {
            'record_ids': record
        }
        #



    
    
