package org.graalphp.nodes;

import com.oracle.truffle.api.CompilerAsserts;
import com.oracle.truffle.api.frame.VirtualFrame;
import com.oracle.truffle.api.nodes.DirectCallNode;

/**
 * Models a invocation of a non polymorphic function in php
 *
 * @author abertschi
 */
public class PhpInvokeNode extends PhpExprNode {

    @Children
    protected PhpExprNode[] argNodes;

    // TODO: investigate
    @Child
    protected DirectCallNode target;


    public PhpInvokeNode(PhpExprNode[] arguments, DirectCallNode target) {
        this.argNodes = arguments;
        this.target = target;
    }

    @Override
    public Object executeGeneric(VirtualFrame frame) {
        // TOOD: what if fewer arguments are passed?
        CompilerAsserts.compilationConstant(argNodes.length);

        Object[] argVals = new Object[argNodes.length];
        for (int i = 0; i < argNodes.length; i++) {
            argVals[i] = argNodes[i].executeGeneric(frame);
        }

        return target.call(argVals);
    }
}
