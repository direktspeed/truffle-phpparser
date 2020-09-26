package org.trufflephp.nodes.function;

import com.oracle.truffle.api.frame.VirtualFrame;
import com.oracle.truffle.api.profiles.BranchProfile;
import org.trufflephp.nodes.PhpExprNode;
import org.trufflephp.nodes.PhpStmtNode;
import org.trufflephp.nodes.controlflow.PhpReturnException;
import org.trufflephp.types.PhpNull;

/**
 * Node to represent a construct in PHP which can return a value
 * (function, or return from global scope)
 * <p>
 * Uses Truffle idiomatic way to wrap return type into Control Flow exception.
 *
 * @author abertschi
 */
public final class PhpReturnBodyNode extends PhpExprNode {

    private final BranchProfile continueTaken = BranchProfile.create();

    @Child
    private PhpStmtNode body;

    public PhpReturnBodyNode(PhpStmtNode body) {
        this.body = body;
    }

    @Override
    public Object executeGeneric(VirtualFrame frame) {
        try {
            body.executeVoid(frame);
        } catch (PhpReturnException e) {
            continueTaken.enter();
            return e.getReturnValue();
        }
        return PhpNull.SINGLETON;
    }


    @Override
    public String toString() {
        return "PhpReturnBodyNode{" +
                ", body=" + body +
                '}';
    }
}
