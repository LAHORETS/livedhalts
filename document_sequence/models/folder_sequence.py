from odoo import models, fields, api



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
                self.complete_seq = str(self.parent_folder_id.complete_seq) +'.'+ str(self.doc_seq)
                
        return res
    
    
