:: # Copyright 2013, Big Switch Networks, Inc.
:: #
:: # LoxiGen is licensed under the Eclipse Public License, version 1.0 (EPL), with
:: # the following special exception:
:: #
:: # LOXI Exception
:: #
:: # As a special exception to the terms of the EPL, you may distribute libraries
:: # generated by LoxiGen (LoxiGen Libraries) under the terms of your choice, provided
:: # that copyright and licensing notices generated by LoxiGen are not altered or removed
:: # from the LoxiGen Libraries and the notice provided below is (i) included in
:: # the LoxiGen Libraries, if distributed in source code form and (ii) included in any
:: # documentation for the LoxiGen Libraries, if distributed in binary form.
:: #
:: # Notice: "Copyright 2013, Big Switch Networks, Inc. This library was generated by the LoxiGen Compiler."
:: #
:: # You may not use this file except in compliance with the EPL or LOXI Exception. You may obtain
:: # a copy of the EPL at:
:: #
:: # http://www.eclipse.org/legal/epl-v10.html
:: #
:: # Unless required by applicable law or agreed to in writing, software
:: # distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
:: # WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
:: # EPL for the specific language governing permissions and limitations
:: # under the EPL.
::
        q.text("${ofclass.pyname} {")
        with q.group():
            with q.indent(2):
                q.breakable()
:: from py_gen.codegen import Member, LengthMember, TypeMember
:: normal_members = [m for m in ofclass.members if type(m) == Member]
:: first = True
:: for m in normal_members:
:: if not first:
                q.text(","); q.breakable()
:: else:
:: first = False
:: #endif
                q.text("${m.name} = ");
:: if m.name == "xid":
                if self.${m.name} != None:
                    q.text("%#x" % self.${m.name})
                else:
                    q.text('None')
:: elif m.oftype.base == 'of_mac_addr_t':
                q.text(util.pretty_mac(self.${m.name}))
:: elif m.oftype.base == 'uint32_t' and m.name.startswith("ipv4"):
                q.text(util.pretty_ipv4(self.${m.name}))
:: elif m.oftype.base == 'of_wc_bmap_t':
                q.text(util.pretty_wildcards(self.${m.name}))
:: elif m.oftype.base == 'of_port_no_t':
                q.text(util.pretty_port(self.${m.name}))
:: elif m.oftype.base.startswith("uint") and not m.oftype.is_array:
                q.text("%#x" % self.${m.name})
:: else:
                q.pp(self.${m.name})
:: #endif
:: #endfor
            q.breakable()
        q.text('}')
