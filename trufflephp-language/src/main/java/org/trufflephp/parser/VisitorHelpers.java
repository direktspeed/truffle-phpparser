package org.trufflephp.parser;

import com.oracle.truffle.api.frame.FrameSlot;
import com.oracle.truffle.api.frame.FrameSlotKind;
import org.eclipse.php.core.ast.nodes.ASTNode;
import org.trufflephp.nodes.PhpExprNode;
import org.trufflephp.nodes.PhpStmtNode;
import org.trufflephp.nodes.localvar.WriteLocalVarNodeGen;

/**
 * Utilities used by several visitors
 *
 * @author abertschi
 */
public class VisitorHelpers {

    private static void setSourceSection(PhpStmtNode target, ASTNode n) {
        if (target.hasSourceSection()) {
            target.setSourceSection(n.getStart(), n.getLength());
        }
    }

    // write a node with given target name into the current frame
    public static PhpExprNode createLocalAssignment(ParseScope scope,
                                                    String target,
                                                    PhpExprNode source,
                                                    Integer argumentId,
                                                    ASTNode sourceSection) {
        final FrameSlot frameSlot =
                scope.getFrameDesc().findOrAddFrameSlot(target, argumentId, FrameSlotKind.Illegal);
        scope.getVars().put(target, frameSlot);

        PhpExprNode node = WriteLocalVarNodeGen.create(source, frameSlot);
        if (sourceSection != null) {
            setSourceSection(node, sourceSection);
        }
        return node;
    }
}
