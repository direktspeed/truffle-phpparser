package org.trufflephp.nodes.controlflow;

import com.oracle.truffle.api.Truffle;
import com.oracle.truffle.api.frame.VirtualFrame;
import com.oracle.truffle.api.nodes.LoopNode;
import com.oracle.truffle.api.nodes.NodeInfo;
import org.trufflephp.nodes.PhpExprNode;
import org.trufflephp.nodes.PhpStmtNode;
import org.trufflephp.nodes.unary.PhpConvertToBooleanNode;

/**
 * @author abertschi
 */
@NodeInfo(shortName = "while")
public final class PhpWhileNode extends PhpStmtNode {

    @Child
    private LoopNode loopNode;

    public PhpWhileNode(PhpExprNode condition, PhpStmtNode body) {
        this.loopNode = Truffle.getRuntime().createLoopNode(
                new PhpWhileRepeatingNode(PhpConvertToBooleanNode.createAndWrap(condition), body));
    }

    @Override
    public void executeVoid(VirtualFrame frame) {
        loopNode.execute(frame);
    }
}
